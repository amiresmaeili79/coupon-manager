from datetime import datetime

from django.db import transaction
from django.db.models import F
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Coupon, CouponUsage
from .serializers import CouponsSerializer, CouponConsumeSerializer
from ..accounts.models import Account


class CouponsList(ListAPIView):
    queryset = (
        Coupon.objects.filter(used_by__lt=F("capacity"))
        .filter(is_active=True)
        .filter(expire_at__lte=datetime.now())
    )  # only get available coupons
    serializer_class = CouponsSerializer
    permission_classes = (AllowAny,)


class UseCouponView(APIView):
    serializer_class = CouponConsumeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: "Request") -> "Response":
        user: Account = request.user
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            coupon = (
                Coupon.objects.filter(code=serializer.data.get("code"))
                .select_for_update()
                .first()
            )

            if coupon.used_by >= coupon.capacity:
                raise PermissionDenied("Coupon is used")

            _, created = CouponUsage.objects.get_or_create(coupon=coupon, account=user)
            if created:
                coupon.used_by += 1
                user.balance += coupon.balance
                coupon.save(update_fields=["used_by"])
                user.save(update_fields=["balance"])

        if not created:
            raise PermissionDenied("You have used this coupon before")

        return Response(status=status.HTTP_204_NO_CONTENT)
