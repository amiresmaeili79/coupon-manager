from django.contrib import admin
from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "balance", "capacity", "expire_at")
    search_fields = ("code",)
    list_filter = ("expire_at",)
