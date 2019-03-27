from django.db import models
# Create your models here.
from django_prometheus.models import ExportModelOperationsMixin

from registration.models import AbstractModel, RegistrationModel


class PaymentModel(ExportModelOperationsMixin('payment'), AbstractModel):
    """
    Registers a payment for a RegistrationModel
    """
    registration = models.ForeignKey(RegistrationModel, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_registered = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
