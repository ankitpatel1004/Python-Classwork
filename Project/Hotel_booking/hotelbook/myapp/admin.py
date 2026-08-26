from django.contrib import admin
from myapp.models import *

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'room_type',
        'price',
        'capacity',
        'rating',
        'available',
    )

    list_filter = (
        'room_type',
        'available',
    )

    search_fields = (
        'name',
        'description',
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'room',
        'check_in',
        'check_out',
        'guests',
        'total_price',
        'status',
    )

    list_filter = (
        'status',
        'check_in',
        'check_out',
    )

    search_fields = (
        'user__username',
        'room__name',
    )