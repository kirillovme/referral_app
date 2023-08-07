from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserCustom, ReferralCode
from .serializers import UserCustomSerializer
import random
import time


class RequestAuthCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        auth_code = random.randint(1000, 9999)
        # Imitate sending 4-symbols code authorization with a 2-second delay
        time.sleep(2)
        request.session['auth_code'] = auth_code
        request.session['phone_number'] = phone_number
        print(request.session['auth_code'])
        return Response({'message': 'Code sent successfully',
                         'code': auth_code})


class VerifyAuthCodeView(APIView):
    def post(self, request):
        code = int(request.data.get('code'))
        if code == request.session.get('auth_code'):
            phone_number = request.session.get('phone_number')
            user, created = UserCustom.objects.get_or_create(phone_number=phone_number)
            if created:
                invite_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
                while UserCustom.objects.filter(invite_code=invite_code).exists():
                    invite_code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
                user.invite_code = invite_code
                user.save()
            return Response(UserCustomSerializer(user).data)
        return Response({'message': 'Invalid code, please request a new code on auth/request_code/'}, status=400)


class UserCustomView(APIView):
    def get(self, request):
        try:
            user = UserCustom.objects.get(phone_number=request.session.get('phone_number'))
        except UserCustom.DoesNotExist:
            return Response({'message': 'Please, first go to auth/request_code/'}, status=403)
        return Response(UserCustomSerializer(user).data)


class ActivateInviteCodeView(APIView):
    def post(self, request):
        code = request.data.get('invite_code')
        try:
            user = UserCustom.objects.get(phone_number=request.session.get('phone_number'))
        except UserCustom.DoesNotExist:
            return Response({'message': 'Please, first go to auth/request_code/'}, status=403)
        if user.activated_code:
            return Response({'message': 'Code already activated'}, status=400)
        try:
            referrer = UserCustom.objects.get(invite_code=code)
            activation = ReferralCode(referrer=referrer, referred_user=user, invite_code=code)
            activation.save()
            user.activated_code = code
            user.save()
            return Response(UserCustomSerializer(user).data)
        except UserCustom.DoesNotExist:
            return Response({'message': 'Invalid code'}, status=400)
