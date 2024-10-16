from django.contrib import admin
from restaurant.models import Table, Restaurant, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'seats', 'number')
    list_filter = ('seats', 'number')
    search_fields = ('restaurant__name', 'number')


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'phone_number')
    list_filter = ('name',)
    search_fields = ('name', 'address', 'phone_number')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # form = BookingForm
    list_display = ('id', 'table', 'client', 'date_reserved', 'time_reserved', 'duration', 'is_active')
    list_filter = ('table',)
    search_fields = ('table', 'client', 'date_reserved')
