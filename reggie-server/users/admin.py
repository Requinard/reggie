from django.contrib import admin

from users import models


# Register your models here.
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


admin.site.register(models.ProfileModel, ProfileAdmin)
