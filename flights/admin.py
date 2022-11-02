from django.contrib import admin

from .models import Flight,Airport,Passenger

class FlightAdimin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdimin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight,FlightAdimin)
admin.site.register(Passenger,PassengerAdimin)