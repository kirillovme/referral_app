from rest_framework import serializers
from .models import UserCustom, ReferralCode


class ReferralCodeSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='referred_user.phone_number', read_only=True)

    class Meta:
        model = ReferralCode
        fields = ['phone_number']


class UserCustomSerializer(serializers.ModelSerializer):
    referrals = ReferralCodeSerializer(many=True, read_only=True, source='referrals_made')

    class Meta:
        model = UserCustom
        fields = ['phone_number', 'invite_code', 'activated_code', 'referrals']
