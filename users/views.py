from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserAuthenticationSerializer
from django.contrib.auth import authenticate
import random
from twilio.rest import Client
from django.core.mail import send_mail


EMAIL_HOST_USER = 'ваш_email@gmail.com'
EMAIL_HOST_PASSWORD = 'ваш_пароль'

verification_codes = {}

@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "Пользователь зарегистрирован!"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    code = random.randint(100000, 999999)

    try:

        send_mail(
            'Ваш код подтверждения',
            f'Ваш код подтверждения: {code}',
            EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        verification_codes[email] = code
        return Response({"message": "Код отправлен!"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"message": f"Ошибка при отправке кода: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def verify(request):
    email = request.data.get('email')
    code = request.data.get('code')

    if email in verification_codes and verification_codes[email] == int(code):
        del verification_codes[email]
        return Response({"message": "Код подтвержден!"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Неверный код!"}, status=status.HTTP_400_BAD_REQUEST)

class AuthorizationApiView(APIView):
    def post(self, request):
        serializer = UserAuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            return Response({"message": "Пользователь авторизован!"}, status=status.HTTP_200_OK)
        return Response({"message": "Неправильные имя пользователя или пароль."}, status=status.HTTP_404_NOT_FOUND)
