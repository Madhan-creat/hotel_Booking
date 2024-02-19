from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RoomType(models.Model):
    TYPES = [
        ('NORMAL', 'NORMAL'),
        ('DELUXE', 'DELUXE'),
        ('STUDIO', 'STUDIO'),
        ('SUITE', 'SUITE'),
        ('KING_ROOM', 'KING_ROOM')
    ]
    room_type_name = models.CharField(choices=TYPES, max_length=120)
    price = models.IntegerField()
    available_count = models.IntegerField()

    def __str__(self):
        return self.room_type_name

class Hotel(models.Model):
    name = models.CharField(max_length=120)
    room_types = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    
class RoomBooking(models.Model):
    STATUSES = [('PENDING','PENDING'),('BOOKED','BOOKED'), ('CANCELLED','CANCELLED')]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUSES, max_length=120)
    check_in_on = models.DateField()
    check_out_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.room_type.room_type_name + " " +str(self.check_in_on)