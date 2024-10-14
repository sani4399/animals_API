from django.contrib import admin
from .models import Animal, Master

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'weight')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'age', 'weight', 'master')
