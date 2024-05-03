from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField()
    file = models.FileField()
    address = models.TextField(blank=True)
    
class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField(default=50)   
    def __str__(self) -> str:
        return f"{self.car_name},{self.speed}"