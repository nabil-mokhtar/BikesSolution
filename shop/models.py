from django.db import models



class branches(models.Model):
    name=models.CharField(max_length=20)
    admin=models.CharField(max_length=20)  #relation to admins 
    def __str__(self):
        return self.name



class Bike(models.Model):
    model=models.CharField(max_length=30)    #phoenix
    serial=models.CharField(max_length=30)   #R300
    image=models.ImageField()
    availability=models.BooleanField()
    availabilityDuration=models.DurationField()  #available for renting in 3 days
    rentability=models.BooleanField()
    used=models.BooleanField()
    description=models.TextField(max_length=100)
    sellPrice=models.IntegerField()
    rentPerDay=models.IntegerField()
    rentPerWeek=models.IntegerField()
    rentPerMonth=models.IntegerField()
    branche=models.ForeignKey(branches,on_delete=models.CASCADE)
    def __str__(self):
        return self.model



class RentUser(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    adress=models.CharField(max_length=30)
    idImage=models.ImageField()
    
    def __str__(self):
        return self.name



class product(models.Model):
    name=models.CharField(max_length=20)
    sellPrice=models.IntegerField()
    image=models.ImageField()
    availability=models.BooleanField()
    branche=models.ForeignKey(branches,on_delete=models.CASCADE)
    def __str__(self):
        return self.name




class Service(models.Model):
    name=models.CharField(max_length=30)
    duration=models.DurationField()
    price=models.IntegerField()
    def __str__(self):
        return self.name



class RentRecords(models.Model):
    customer=models.ForeignKey(RentUser,on_delete=models.CASCADE)
    bike=models.ForeignKey(Bike,on_delete=models.CASCADE)
    starts=models.DateTimeField()
    ends=models.DateTimeField()
    status=models.CharField(max_length=10)
    note=models.CharField(max_length=50)
    price=models.IntegerField()

    def __str__(self):
        return self.status

