from rest_framework import serializers
from .models import CustomUser
from rest_framework.exceptions import ValidationError

class UserAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = CustomUser.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            raise ValidationError("Неправильные имя пользователя или пароль.")

        return attrs

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    name = serializers.CharField()
    surname = serializers.CharField()
    email = serializers.EmailField()

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Пользователь с таким именем уже существует!")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Пользователь с таким email уже существует!")
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if password != password_confirm:
            raise ValidationError("Пароли не совпадают.")

        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['name'],
            last_name=validated_data['surname']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
