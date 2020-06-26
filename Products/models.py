from django.db import models

# Create your models here.


class branches(models.Model):
    name=models.CharField(max_length=20)
    admin=models.CharField(max_length=20)  #relation to admins 
    def __str__(self):
        return self.name



class Bike(models.Model):
    model=models.CharField(max_length=30)    #phoenix
    serial=models.CharField(max_length=30)   #R300
    image=models.ImageField()

    availability=models.BooleanField() #both rent and sell
    rentability=models.BooleanField()  

    availabilityDuration=models.DurationField()  #available for renting in 3 days
   
    #used=models.BooleanField()
    description=models.TextField(max_length=100)
    sellPrice=models.IntegerField()
    rentPerDay=models.IntegerField()
    rentPerWeek=models.IntegerField()
    rentPerMonth=models.IntegerField()
    branche=models.ForeignKey(branches,on_delete=models.PROTECT)
    def __str__(self):
        return self.model


class Service(models.Model):
    name=models.CharField(max_length=30)
    duration=models.DurationField()
    price=models.IntegerField()
    def __str__(self):
        return self.name


class accessories(models.Model):
    name=models.CharField(max_length=20)
    sellPrice=models.IntegerField()
    image=models.ImageField()
    availability=models.BooleanField()
    branche=models.ForeignKey(branches,on_delete=models.PROTECT)
    def __str__(self):
        return self.name
