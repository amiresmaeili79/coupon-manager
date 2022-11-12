from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username is None or password is None:
            raise serializers.ValidationError(
                "Username and password are required to login"
            )

        return attrs
