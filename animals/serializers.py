from rest_framework import serializers
from .models import Animal, Master

class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ['id', 'name', 'surname', 'age', 'weight']


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'title', 'name', 'nickname', 'age', 'weight']


    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("ошибка")
        return value
