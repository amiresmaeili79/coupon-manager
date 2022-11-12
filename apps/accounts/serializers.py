from rest_framework import serializers

from apps.accounts.models import Account


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


class AccountsBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username", "balance", "date_joined")


class AccountDetailedSerializer(AccountsBasicSerializer):
    class Meta(AccountsBasicSerializer.Meta):
        fields = AccountsBasicSerializer.Meta.fields + (
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
        )


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "first_name",
            "last_name",
            "email",
        )
