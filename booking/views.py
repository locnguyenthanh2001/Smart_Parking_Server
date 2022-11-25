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


from .models import Booking
from .serializers import BookingSerializer

class BookingViewset(viewsets.ModelViewSet):
    serializer_class=BookingSerializer
    queryset=Booking.objects.all()

    # def post(self, request):
    #     """Create a hello message with our name"""
    #     serializer = self.serializer_class(data=request.data)

    #     if serializer.is_valid():
    #         name = serializer.validated_data.get('name')
    #         message = f'Created {name}'
    #         return Response({'message':message})
    #     else:
    #         return Response(
    #             serializer.errors,
    #             status=status.HTTP_400_BAD_REQUEST
    #         )