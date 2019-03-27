from django.db import models

# Create your models here.
from registration.models import AbstractModel, RegistrationModel, ConventionModel


class HotelModel(AbstractModel):
    """
    Holds data for a hotel
    """
    name = models.CharField(max_length=60, unique=True)
    conventions = models.ManyToManyField(ConventionModel, blank=True, related_name="hotels")
    is_public = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hotel"


class FloorModel(AbstractModel):
    name = models.CharField(max_length=40)
    hotel = models.ForeignKey(HotelModel, related_name="floors", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Floor"


class RoomModel(AbstractModel):
    name = models.CharField(max_length=10, blank=True, null=True)
    hotel = models.ForeignKey(HotelModel, related_name="rooms", on_delete=models.CASCADE)
    floor = models.ForeignKey(FloorModel, related_name="rooms", on_delete=models.CASCADE)

    type = models.SmallIntegerField(choices=(
        (1, "regular"),
        (2, "deluxe"),
        (3, "junior suite"),
        (4, "suite"),
        (5, "penthouse"),
    ))
    capacity = models.CharField(max_length=6, choices=(
        ('B', 'Single bed'),
        ('BB', 'Double bed'),
        ('B B', 'Two single beds'),
        ('BB B', 'Double and Single bed'),
        ('BB BB', 'Two double beds'),
    ))
    capacity_extra = models.PositiveSmallIntegerField(
        default=0,
        help_text="Extra capacity that can possibly be added to the room"
    )

    # Room Locking
    is_locked = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    password = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        verbose_name = "Room"


class RoomReservationModel(AbstractModel):
    """
    Connects a room to a reservation
    """
    room = models.ForeignKey(RoomModel, related_name="reservations", on_delete=models.CASCADE)
    registration = models.ForeignKey(RegistrationModel, related_name="reservations", on_delete=models.CASCADE)
    is_extra_capacity = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Room Reservation"
