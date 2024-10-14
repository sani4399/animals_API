# urls.py
from django.urls import path
from .views import (
    registration_api_view,
    AuthorizationApiView,
    register,
    verify
)

urlpatterns = [
    path('registration/', registration_api_view, name='registration'),
    path('authorization/', AuthorizationApiView.as_view(), name='authorization'),
    path('send-code/', register, name='send-code'),
    path('verify-code/', verify, name='verify-code'),
]
