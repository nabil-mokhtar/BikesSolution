from rest_framework import serializers
from . import models


class RentRecordsserializers(serializers.ModelSerializer):

    class Meta:
        model = models.RentRecords
        fields = ('id', 'customer', 'bike', 'status',
                  'ends', 'note', 'price', 'adminName')


class FixRecordsserializers(serializers.ModelSerializer):

    class Meta:
        model = models.FixRecords
        fields = ('id', 'customer', 'price',
                  'notes', 'url', 'adminName')


class SellRecordserializers(serializers.ModelSerializer):

    class Meta:
        model = models.SellRecord
        fields = ('id', 'customer', 'price', 'product', 'dateTime',
                  'notes', 'adminName')


class Noterecordserializers(serializers.ModelSerializer):

    class Meta:
        model = models.Noterecord
        fields = ('id', 'customer', 'price', 'note', 'url')
