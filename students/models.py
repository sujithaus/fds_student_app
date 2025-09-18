

# Create your models here.
from django.db import models

class Student(models.Model):
    roll_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    subject1 = models.CharField(max_length=100)
    marks1 = models.IntegerField()
    subject2 = models.CharField(max_length=100)
    marks2 = models.IntegerField()
    subject3 = models.CharField(max_length=100)
    marks3 = models.IntegerField()

    def __str__(self):
        return f"{self.roll_number} - {self.name}"
