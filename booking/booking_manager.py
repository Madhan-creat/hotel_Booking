from datetime import datetime, timedelta
from .models import RoomBooking

class BookingManager():
    def __init__(self, hotel, room_type, user) -> None:
        self.hotel = hotel
        self.room_type = room_type
        self.user = user

    def generate_date_range(start_date, end_date):
        date_range = []
        current_date = start_date
        while current_date <= end_date:
            date_range.append(current_date)
            current_date += timedelta(days=1)
        return tuple(date_range)
    
    def is_available(self, start_date, end_date):
        is_available = True
        dates = self.generate_date_range(start_date, end_date)
        for date_obj in dates:
            if RoomBooking.objects.filter(
                hotel=self.hotel,
                room_type=self.room_type,
                check_in_on__lte=date_obj,
                check_out_on__gte= date_obj+timedelta(days=1),
                status="BOOKED"     
            ).count >= self.room_type.available_count:
                is_available = False
                break
        return is_available
    
    def create_booking(self, start_date, end_date):
        bookings = []
        dates = self.generate_date_range(start_date, end_date)
        for date_obj in dates:
            bookings.append(RoomBooking.objects.create(
                hotel=self.hotel,
                room_type=self.room_type,
                check_in_on=date_obj,
                check_out_on= date_obj+timedelta(days=1),
                status="BOOKED",
                user=self.user
            ))
        return bookings