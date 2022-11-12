from rest_framework import serializers

from .models import Coupon


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ("code", "balance", "capacity", "used_by", "expire_at")
