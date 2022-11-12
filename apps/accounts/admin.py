from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ("username", "balance", "date_joined")
    search_fields = ("username", "id")
    list_filter = ("is_superuser", "is_staff")

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in obj._meta.fields if not f.editable]
