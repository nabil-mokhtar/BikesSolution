from django.contrib import admin
from . models import Bike, accessories, Service, BikeImage


class BikeImageAdmin(admin.StackedInline):
    min_num = 0
    max_num = 4
    model = BikeImage


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    inlines = [BikeImageAdmin]

    class Meta:
        model = Bike


@admin.register(BikeImage)
class BikeImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(accessories)
admin.site.register(Service)
