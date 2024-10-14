from django.urls import path
from .views import AnimalListCreate, AnimalDetail,  MasterListCreate

urlpatterns = [
    path('animals/', AnimalListCreate.as_view(), name='animal-list-create'),
    path('animals/<int:pk>/', AnimalDetail.as_view(), name='animal-detail'),
    path('master/', MasterListCreate.as_view(), name='master-list-create'),
    path('master/int:pk/', MasterListCreate.as_view(), name='master-list-detail'),
]
