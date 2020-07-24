from django.db import models
from Users.models import User
from Products.models import Bike, accessories

# Create your models here.


class RentRecords(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    starts = models.DateTimeField(auto_now=True)
    ends = models.CharField(max_length=30)
    status = models.BooleanField()
    note = models.CharField(max_length=50)
    price = models.IntegerField()
    adminName = models.CharField(max_length=20)

    def __str__(self):
        return str(self.status)


class FixRecords(models.Model):
    # we need to make defult customer to unsaved users
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    dateTime = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=100)
    adminName = models.CharField(max_length=20)


class SellRecord(models.Model):
    # we need to make defult customer to unsaved users
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    product = models.CharField(max_length=30)
    dateTime = models.DateTimeField(auto_now=True)
    notes = models.TextField()
    adminName = models.CharField(max_length=20)


class Noterecord(models.Model):
    # we need to make defult customer to unsaved users
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.IntegerField()
    note = models.TextField(max_length=100)
