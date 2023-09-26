from django.contrib import admin

from .models import *
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
class AirportAdmin(admin.ModelAdmin):
    list_display = ("code","city")
class PassengerAdmin(admin.ModelAdmin):
    list_display = ("first","last")
    filter_horizontal = ("flights",)

admin.site.register(Airport,AirportAdmin)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,PassengerAdmin)