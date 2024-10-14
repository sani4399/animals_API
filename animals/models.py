from django.db import models

class Master(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.IntegerField()
    of = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Animal(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=150)
    age = models.IntegerField()
    weight = models.IntegerField()
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='animals')

    def __str__(self):
        return self.name

