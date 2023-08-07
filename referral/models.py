from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class UserCustom(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, null=True, blank=True, unique=True)
    activated_code = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number or 'User without phone number'


class ReferralCode(models.Model):
    referrer = models.ForeignKey(UserCustom, related_name='referrals_made', on_delete=models.CASCADE)
    referred_user = models.ForeignKey(UserCustom, related_name='referrals_received', on_delete=models.CASCADE)
    invite_code = models.CharField(max_length=6)
