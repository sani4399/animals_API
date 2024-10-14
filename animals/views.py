from django.shortcuts import render
from rest_framework import generics
from .models import Animal, Master
from .serializers import AnimalSerializer, MasterSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'Total': self.page.paginator.count,
            'results': data,
        })

class CustomPagination(PageNumberPagination):
    page_size = 2

class MasterListCreate(generics.ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    pagination_class = CustomPagination

class MasterlistCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

class AnimalListCreate(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    pagination_class = CustomPagination

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

