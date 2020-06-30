from rest_framework import serializers
from . import models


class RentRecordsserializers(serializers.ModelSerializer):

    class Meta:
        model = models.RentRecords
        fields = ('id', 'customer', 'bike', 'starts',
                  'ends', 'status', 'note', 'price', 'url')


class FixRecordsserializers(serializers.ModelSerializer):

    class Meta:
        model = models.FixRecords
        fields = ('id', 'customer', 'price', 'dateTime',
                  'notes', 'url')


class SellBRecordserializers(serializers.ModelSerializer):

    class Meta:
        model = models.SellBRecord
        fields = ('id', 'customer', 'price', 'bike',
                  'dateTime', 'notes', 'url')


class SellARecordserializers(serializers.ModelSerializer):

    class Meta:
        model = models.SellARecord
        fields = ('id', 'customer', 'price', 'accessorie',
                  'dateTime', 'notes', 'url')


class Noterecordserializers(serializers.ModelSerializer):

    class Meta:
        model = models.Noterecord
        fields = ('id', 'customer', 'price', 'note', 'url')
