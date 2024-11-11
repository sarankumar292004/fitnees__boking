from django.contrib import admin
from .models import FitnessClass, Booking

class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'end_time', 'max_participants')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('fitness_class', 'booking_date')  # Removed 'user'

admin.site.register(FitnessClass, FitnessClassAdmin)
admin.site.register(Booking, BookingAdmin)
