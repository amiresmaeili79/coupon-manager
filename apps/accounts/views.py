from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Account
from .serializers import (
    LoginSerializer,
    AccountsBasicSerializer,
    AccountDetailedSerializer,
    ProfileUpdateSerializer,
)


class LoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request: "Request") -> "Response":
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user: Account = authenticate(
            username=serializer.data.get("username"),
            password=serializer.data.get("password"),
        )
        if (user is None) or (not user.is_active):
            return Response(
                "Username or password is not correct",
                status=status.HTTP_401_UNAUTHORIZED,
            )

        return Response(user.tokens, status=status.HTTP_200_OK)


class Profile(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        method_mapping = {
            "GET": AccountDetailedSerializer,
            "PATCH": ProfileUpdateSerializer,
            "PUT": ProfileUpdateSerializer,
        }

        return method_mapping.get(self.request.method)


class AccountViewSet(ReadOnlyModelViewSet):
    queryset = Account.objects.all()

    def get_serializer_class(self):
        serializer_mapping = {
            "list": AccountsBasicSerializer,
            "retrieve": AccountDetailedSerializer,
        }
        return serializer_mapping.get(self.action, serializer_mapping["list"])
