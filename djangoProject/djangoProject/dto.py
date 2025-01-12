from rest_framework import serializers
from .models import VehicleData
class VehicleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleData
        fields = '__all__'
        extra_kwargs = {
            'url': {'required': True},
            'title': {'required': True},
        }