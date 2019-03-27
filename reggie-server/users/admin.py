from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users import models


class WarningInline(admin.TabularInline):
    model = models.WarningModel
    extra = 0


class BanInline(admin.TabularInline):
    model = models.BanModel
    extra = 0


# Register your models here.
@admin.register(models.ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_private_profile', 'gender', 'address_city', 'address_country')
    list_filter = ('gender', 'is_private_profile', 'shirt_size')

    search_fields = ('address_street', 'address_city', 'address_postal_code', 'address_country')

    fieldsets = (
        ('Relational Information', {
            'fields': ('user',)
        }),
        ('Address information', {
            'fields': (('address_street', 'address_number'), ('address_postal_code', 'address_city'), 'address_country')
        }),
        ('Personal information', {
            'fields': ('date_of_birth', 'phone_number', 'gender', 'shirt_size')
        }),
        ('Extra comments', {
            'fields': ('profile_comments', 'profile_private_comments')
        }),
        ('Switches', {
            'fields': ('is_private_profile',)
        })
    )


@admin.register(models.WarningModel)
class WarningAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BanModel)
class BanADmin(admin.ModelAdmin):
    pass


class UserAdmin(BaseUserAdmin):
    inlines = [
        WarningInline,
        BanInline
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
