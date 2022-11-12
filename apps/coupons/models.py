from django.db import models

from apps.shared.models import FeaturedBaseModel
from apps.accounts.models import Account


class Coupon(FeaturedBaseModel):
    code = models.CharField(max_length=50, db_index=True)
    balance = models.PositiveBigIntegerField(default=0)
    capacity = models.PositiveIntegerField()
    used_by = models.PositiveIntegerField()
    expire_at = models.DateTimeField()

    def __str__(self):
        return self.code

    def __repr__(self):
        return f"Coupon({self.code}, {self.balance}, {self.capacity}, {self.expire_at})"

    class Meta:
        db_table = "coupons"
        ordering = ("expire_at",)


class CouponUsage(FeaturedBaseModel):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True
    )  # in case of account deletion, consistency of coupon capacity should be remained
