from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import LoginSerializer


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
