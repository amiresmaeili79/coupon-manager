from django.urls import path

from .views import CouponsList, UseCouponView

app_name = "coupons"

urlpatterns = [
    path("", CouponsList.as_view(), name="all_coupons"),
    path("use/", UseCouponView.as_view(), name="use"),
]
