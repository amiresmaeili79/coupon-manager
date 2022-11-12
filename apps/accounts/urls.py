from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LoginView, AccountViewSet

app_name = "accounts"

router = DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="accounts")

urlpatterns = [path("login/", LoginView.as_view(), name="login")]
urlpatterns += router.urls
