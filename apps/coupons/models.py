from apps.shared.models import FeaturedBaseModel
from django.db import models


class Coupon(FeaturedBaseModel):
    code = models.CharField(max_length=50, db_index=True)
    balance = models.PositiveBigIntegerField(default=0)
    capacity = models.PositiveIntegerField()
    expire_at = models.DateTimeField()

    def __str__(self):
        return self.code

    def __repr__(self):
        return f"Coupon({self.code}, {self.balance}, {self.capacity}, {self.expire_at})"

    class Meta:
        db_table = "coupons"
        ordering = ("expire_at",)
