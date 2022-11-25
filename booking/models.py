import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from parking_lot.models import ParkingLot
from profiles_api.models import UserProfile

BOOKING_STATUS = (
    ('BOOKED', 'Booked'),
    ('PARKING', 'Parking'),
    ('FINSHED', 'Finished'),
    ('CANCEL', 'Cancel'),
)




class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile, related_name='user', on_delete=models.CASCADE)
    parking_lot = models.ForeignKey(ParkingLot, related_name='parking_lot', on_delete=models.CASCADE)
    booking_duration = models.FloatField(default=10)
    status = models.CharField(max_length=10,choices=BOOKING_STATUS, default='BOOKED')
    created_on = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['booking_duration', 'status', 'created_on']

    def __str__(self):
        return self.id
