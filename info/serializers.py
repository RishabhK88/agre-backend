from rest_framework import serializers

from .models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('type', 'health', 'temperature', 'moisture', 'nitrogen', 'phosphorus', 'potassium')