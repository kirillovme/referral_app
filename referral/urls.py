from django.urls import path
from .views import RequestAuthCodeView, VerifyAuthCodeView, UserCustomView, ActivateInviteCodeView

urlpatterns = [
    path('auth/request_code/', RequestAuthCodeView.as_view(), name='request_code'),
    path('auth/verify_code/', VerifyAuthCodeView.as_view(), name='verify_code'),
    path('profile/', UserCustomView.as_view(), name='profile'),
    path('activate_code/', ActivateInviteCodeView.as_view(), name='activate_code'),
]