from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import FeaturedBaseModel


class Account(AbstractUser, FeaturedBaseModel):
    balance = models.PositiveBigIntegerField(default=0)

    class Meta:
        db_table = "accounts"
