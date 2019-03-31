import uuid as uuid
from datetime import datetime
from django.contrib.auth import models as user
from django.db import models
# Create your models here.
from django_prometheus.models import ExportModelOperationsMixin


class AbstractModel(models.Model):
    """
    Holds data that all classes should use
    """
    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class ConventionModel(AbstractModel):
    """
    Holds the data for a specific instance of a convention.
    """
    name = models.CharField(max_length=200)
    con_event_start_date = models.DateField()
    con_event_close_date = models.DateField()
    con_reg_start_time = models.DateTimeField()
    con_reg_close_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Switches
    is_public = models.BooleanField(default=False)
    uses_hotel_mode = models.BooleanField(default=False)

    def reg_is_open(self):
        return datetime.utcnow() >= self.con_reg_time

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Convention"


class RegistrationModel(ExportModelOperationsMixin('registration'), AbstractModel):
    """
    Connects a User to a Convention and adds reg metadata
    """
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
    convention = models.ForeignKey(ConventionModel, on_delete=models.CASCADE, related_name='registrations')
    is_accepted = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)

    membership_level = models.SmallIntegerField(default=0, choices=(
        (0, "Attendee"),
        (1, "Staff"),
        (2, "Helper"),
        (3, "Organisation"),
        (4, "Director")
    ))

    class Meta:
        unique_together = ('user', 'convention')

    def save(self, *args, **kwargs):
        if self.is_accepted:
            self.is_pending = False

        super(RegistrationModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return "{0} @ {1} ({2})".format(self.user, self.convention, self.uuid)

    def get_badge_number(self):
        return RegistrationModel.objects.filter(convention=self.convention, date_created__lt=self.date_created).count()

    class Meta:
        verbose_name = "Registration"
        indexes = [
            models.Index(fields=['id', 'user']),
            models.Index(fields=['id', ]),
            models.Index(fields=['user', ])
        ]


class RegistrationAddinModel(ExportModelOperationsMixin('registation_addin'), AbstractModel):
    """
    Extra items that can be added to a registration
    """
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    registrations_added_to = models.ManyToManyField(RegistrationModel, related_name="addons", blank=True)
    convention = models.ForeignKey(ConventionModel, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} @ {1} ({2})".format(self.name, self.convention, self.uuid)

    class Meta:
        verbose_name = "Registration Add-In"
        verbose_name_plural = "Registration Add-Ins"
