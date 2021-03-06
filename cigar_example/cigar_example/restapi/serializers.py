from rest_framework import serializers
from rest_framework import fields
from cigar_example.app import models
from django.db.models.base import get_absolute_url


class CigarSerializer(serializers.ModelSerializer):
    manufacturer_id = fields.WritableField()
    url = fields.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Cigar


class ManufacturerSerializer(serializers.ModelSerializer):
    country_id = fields.WritableField()

    class Meta:
        model = models.Manufacturer


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Countries
