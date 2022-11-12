from django.db.models import F
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Coupon

from .serializers import CouponsSerializer


class CouponsList(ListAPIView):
    queryset = Coupon.objects.filter(used_by__lt=F("capacity"))
    serializer_class = CouponsSerializer
    permission_classes = (AllowAny,)
