from django.contrib import admin

# Register your models here.
from bookings import models


class FloorInline(admin.StackedInline):
    model = models.FloorModel


class RoomInline(admin.StackedInline):
    model = models.RoomModel


@admin.register(models.HotelModel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(models.RoomModel)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'hotel', 'type', 'capacity', 'is_locked')
    search_fields = ('name',)
    list_filter = ('hotel', 'hotel__conventions', 'is_locked', 'capacity', 'type')

    fieldsets = (
        ('Metadata', {
            'fields': (('name', 'hotel'),)
        }),
        ('Capacity', {
            'fields': ('type', ('capacity', 'capacity_extra'))
        }),
        ('Locks', {
            'fields': (('is_locked', 'password'),)
        })
    )


@admin.register(models.FloorModel)
class FloorAdmin(admin.ModelAdmin):
    pass
