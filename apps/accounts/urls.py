from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import LoginView, AccountViewSet, Profile

app_name = "accounts"

router = DefaultRouter()
router.register(r"accounts", AccountViewSet, basename="accounts")

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", Profile.as_view(), name="profile"),
]
urlpatterns += router.urls
