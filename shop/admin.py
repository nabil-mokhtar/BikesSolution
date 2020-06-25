from django.contrib import admin
from .models import Bike,product,RentUser,Service


admin.site.register(Bike)

admin.site.register(product)

admin.site.register(Service)

# admin.site.register(RentUser)