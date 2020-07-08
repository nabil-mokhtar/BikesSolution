from rest_framework import serializers
from shop.models import RentRecords


class RentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RentRecords
        fields = ('starts', 'ends', 'price')
