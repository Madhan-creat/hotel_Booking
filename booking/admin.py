from django.contrib import admin
from .models import RoomType, Hotel, RoomBooking

admin.site.register(RoomType)
admin.site.register(Hotel)
admin.site.register(RoomBooking)
