from .models import ParkingLot
from rest_framework import serializers

class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta:
        model=ParkingLot
        fields='__all__'
    
