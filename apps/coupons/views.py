from datetime import datetime

from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Coupon
from .serializers import CouponsSerializer


class CouponsList(ListAPIView):
    queryset = (
        Coupon.objects.filter(used_by__lt=F("capacity"))
        .filter(is_active=True)
        .filter(expire_at__lte=datetime.now())
    )  # only get available coupons
    serializer_class = CouponsSerializer
    permission_classes = (AllowAny,)
