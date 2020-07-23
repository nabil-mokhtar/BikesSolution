from rest_framework import serializers
from .models import User, RentReservations, FixReservations


class Userserializers(serializers.ModelSerializer):

    class Meta:
        model = User
        image = serializers.SerializerMethodField('get_image')

        def get_image(self, obj):
            try:
                image = obj.image.url
            except:
                image = None
            return image
        fields = ('id', 'name', 'phone', 'adress',
                  'idImage', 'url', 'userimage')
        # fields = '__all__'


class RentReservationsserializers(serializers.ModelSerializer):

    class Meta:
        model = RentReservations

        fields = ('id', 'user', 'bike', 'startDateTime',
                  'notes', 'duration', 'url')


class FixReservationsserializers(serializers.ModelSerializer):

    class Meta:
        model = FixReservations

        fields = ('id', 'user', 'service', 'notes',
                  'dateTime', 'url')
