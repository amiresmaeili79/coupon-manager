from django.urls import path

from .views import CouponsList

app_name = "coupons"

urlpatterns = [path("", CouponsList.as_view(), name="all_coupons")]
