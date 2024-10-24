from rest_framework import serializers
from scarping.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'brand',
            'model',
            'car_class',
            'fuel',
            'seat_count',
            'segment',
            'transmission',
            'vendor',
            'check_in_datetime',
            'check_in_office',
            'check_out_datetime',
            'check_out_office',
        ]
