from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import FeaturedBaseModel
from rest_framework_simplejwt.tokens import RefreshToken


class Account(AbstractUser, FeaturedBaseModel):
    balance = models.PositiveBigIntegerField(default=0)

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"access": str(refresh.access_token), "refresh": str(refresh)}

    class Meta:
        db_table = "accounts"
