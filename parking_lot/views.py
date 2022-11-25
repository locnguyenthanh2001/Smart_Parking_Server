from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from .models import  ParkingLot
from .serializers import  ParkingLotSerializer

class ParkingLotViewset(viewsets.ModelViewSet):
    serializer_class=ParkingLotSerializer
    queryset=ParkingLot.objects.all()

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
