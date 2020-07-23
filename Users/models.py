from django.db import models
from Products.models import Bike, Service

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    adress = models.CharField(max_length=30)
    idImage = models.ImageField()
    userimage=models.ImageField()

    def __str__(self):
        return self.name


class RentReservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    startDateTime = models.DateTimeField()
    notes = models.TextField(max_length=100)
    duration = models.DurationField()


class FixReservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    notes = models.TextField(max_length=100)
    dateTime = models.DateTimeField()
