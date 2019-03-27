from django.contrib import admin

from payments import models

# Register your models here.
metadata_fields = ("Metadata", {
    'fields': ('date_created', 'date_edited', 'uuid'),
    'classes': ['collapse', ]
})


class PaymentInline(admin.StackedInline):
    model = models.PaymentModel
    classes = ['collapse', ]

    fields = ('registration', ('amount', 'date_registered'), 'notes')


@admin.register(models.PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('registration', 'amount', 'date_registered')
    list_filter = ('date_registered', 'date_edited')
