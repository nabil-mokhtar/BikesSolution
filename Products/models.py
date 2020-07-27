from django.db import models
from django.conf import settings

# Create your models here.


class Bike(models.Model):
    model = models.CharField(max_length=30)  # phoenix
    serial = models.CharField(max_length=30)  # R300
    image = models.ImageField()
    availability = models.BooleanField()  # both rent and sell
    rentability = models.BooleanField()
    availabilityDuration = models.CharField(
        max_length=20)  # available for renting in 3 days
    # used=models.BooleanField()
    description = models.TextField(max_length=300)
    sellPrice = models.IntegerField()
    rentPerDay = models.IntegerField()
    rentPerWeek = models.IntegerField()
    rentPerMonth = models.IntegerField()
    branche = models.CharField(max_length=30)

    def __str__(self):
        return self.model


class BikeImage(models.Model):
    Bike = models.ForeignKey(
        Bike, default=None, on_delete=models.CASCADE, related_name='images')
    images = models.FileField(upload_to='images/')

    def __str__(self):
        return self.Bike.model

    @property
    def image_url(self):
        return "{0}".format(self.images.url)


class Service(models.Model):
    name = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
    price = models.IntegerField()
    notes = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class accessories(models.Model):
    name = models.CharField(max_length=20)
    sellPrice = models.IntegerField()
    image = models.ImageField()
    availability = models.BooleanField()
    branche = models.CharField(max_length=30)

    def __str__(self):
        return self.name
