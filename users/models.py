from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Animal(models.Model):
    name = models.CharField(max_length=100)
    master = models.ForeignKey('Master', related_name='animals', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Master(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
