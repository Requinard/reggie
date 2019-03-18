from django.contrib import admin
from registration import models

metadata_fields = ("Metadata", {
    'fields': ('date_created', 'date_edited', 'uuid'),
    'classes': ['collapse', ]
})


# Register your models here.
class PaymentInline(admin.StackedInline):
    model = models.PaymentModel

    verbose_name = "Payment"
    verbose_name_plural = "Payments"
    classes = ['collapse', ]

    fields = ('registration', ('amount', 'date_registered'), 'notes')


class RegistrationAddinInline(admin.StackedInline):
    model = models.RegistrationAddinModel

    verbose_name = "Registration Addin"
    verbose_name_plural = "Registration Addins"
    classes = ["collapse", ]


@admin.register(models.ConventionModel)
class ConventionAdmin(admin.ModelAdmin):
    list_display = ('name', 'con_event_start_date', 'con_event_close_date', 'con_reg_start_time', 'price', 'date_edited')
    list_filter = ('con_event_start_date', 'con_event_close_date', 'con_reg_start_time', 'con_reg_close_time', 'date_edited', 'date_created')
    inlines = [
        RegistrationAddinInline
    ]

    fieldsets = (
        ("Con Info", {
            "fields": (
            'name', ('con_event_start_date', 'con_event_close_date'), ('con_reg_start_time', 'con_reg_close_time'), 'price')
        }),
        metadata_fields,
    )
    readonly_fields = ('date_created', 'date_edited', 'uuid')


@admin.register(models.RegistrationModel)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'convention', 'is_accepted', 'is_pending', 'membership_level')
    list_filter = ('convention', 'is_accepted', 'is_pending', 'date_edited', 'membership_level')
    inlines = [
        PaymentInline
    ]
    fieldsets = (
        ("Attendee Info", {
            'fields': ('user', 'convention')
        }),
        ("Registration Status", {
            'fields': (('is_accepted', 'is_pending'), 'membership_level', 'notes')
        }),
        metadata_fields,
    )

    readonly_fields = ('date_created', 'date_edited', 'uuid')


@admin.register(models.PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('registration', 'amount', 'date_registered')
    list_filter = ('date_registered', 'date_edited')


@admin.register(models.RegistrationAddinModel)
class RegistrationAddinAdmin(admin.ModelAdmin):
    list_display = ('convention', 'name', 'price')
    list_filter = ('convention', 'date_edited')
    search_fields = ('name',)

    fieldsets = (
        ('Information', {
            'fields': ('name', 'description', 'price')
        }),
        ("Relations", {
            'fields': ('convention', 'registrations_added_to')
        }),
        metadata_fields
    )

    readonly_fields = ('date_created', 'date_edited', 'uuid')
