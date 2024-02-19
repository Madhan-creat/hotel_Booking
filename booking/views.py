from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import RoomBooking, RoomType, Hotel
from .serializers import RoomBookingSerializer
from datetime import timedelta
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .booking_manager import BookingManager

class RoomBookingListCreateView(generics.ListCreateAPIView):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        hotel_id = request.data.get('hotel_id')
        room_type_id = request.data.get('room_type_id')
        check_in_date = request.data.get('check_in_date')
        check_out_date = request.data.get('check_out_date')
        try:
            hotel = Hotel.objects.get(id=hotel_id,is_available=True)
            user = User.objects.get(id=user.pk)
            room_type = RoomType.objects.get(id=room_type_id)
        except (User.DoesNotExist, RoomType.DoesNotExist, Hotel.DoesNotExist):
            return Response({'error': 'Hotel, User or RoomType does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        manager = BookingManager(hotel, room_type)

        if not manager.is_available(check_in_date, check_out_date):
            return Response({'error': 'Room not available for the specified date range'}, status=status.HTTP_400_BAD_REQUEST)
        bookings = manager.create_booking()
        serializer = RoomBookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RoomBookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomBooking.objects.all()
    serializer_class = RoomBookingSerializer
