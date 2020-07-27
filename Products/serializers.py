from rest_framework import serializers
from . import models


class Bikeserializers(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None, use_url=True)
    images = serializers.StringRelatedField(many=True, use_url=True)

    class Meta:
        model = models.Bike

        # image = serializers.SerializerMethodField('get_image')

        # def get_image(self, obj):
        #     try:
        #         image = obj.image.url
        #     except:
        #         image = None
        #     return image

        fields = ['id', 'model', 'serial', 'image', 'availability', 'rentability', 'availabilityDuration',
                  'description', 'sellPrice', 'rentPerDay', 'rentPerWeek', 'rentPerMonth', 'branche', 'images']


class Serviceserializers(serializers.ModelSerializer):

    class Meta:
        model = models.Service
        fields = ('id', 'name', 'duration', 'price', 'url')


class accessoriesserializers(serializers.ModelSerializer):

    class Meta:
        model = models.accessories

        image = serializers.SerializerMethodField('get_image')

        def get_image(self, obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image

        fields = ('id', 'name', 'sellPrice', 'image',
                  'availability', 'branche', 'url')
