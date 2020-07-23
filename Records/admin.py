from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.RentRecords)
admin.site.register(models.FixRecords)
admin.site.register(models.SellRecord)
admin.site.register(models.Noterecord)
