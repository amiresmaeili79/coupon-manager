from django.utils import timezone
from rest_framework import serializers

from .models import Coupon


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ("code", "balance", "capacity", "used_by", "expire_at")


class CouponConsumeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)

    def validate(self, attrs):
        if not attrs.get("code"):
            raise serializers.ValidationError("Coupon code is required")

        coupon = Coupon.objects.filter(code=attrs.get("code")).first()
        if (not coupon) or (coupon.expire_at < timezone.now()):
            raise serializers.ValidationError("Given coupon code is not valid")

        return attrs
