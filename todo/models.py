from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name