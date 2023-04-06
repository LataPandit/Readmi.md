from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)

    def __str__(self) -> str:
        return f'{self.name}'