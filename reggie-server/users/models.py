from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileModel(models.Model):
    """
    Overwrite basic model to store extra info.

    Make all fields optional or default unless truly required.
    """
    # Relation
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    # Settings
    is_private_profile = models.BooleanField(default=False)

    # User data
    address_street = models.CharField(max_length=100, blank=True, null=True)
    address_postal_code = models.CharField(max_length=10, blank=True, null=True)
    address_number = models.CharField(max_length=10, blank=True, null=True)
    address_city = models.CharField(max_length=30, blank=True, null=True)
    address_country = models.CharField(max_length=50, blank=True, null=True)

    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.IntegerField(
        choices=(
            (0, "Not specified"),
            (1, "Male"),
            (2, "Female"),
            (3, "Other")
        ),
        default=0
    )
    shirt_size = models.IntegerField(
        choices=(
            (0, "XXS"),
            (1, "XS"),
            (2, "S"),
            (3, "M"),
            (4, "L"),
            (5, "XL"),
            (6, "XXL")
        ),
        null=True,
        blank=True
    )

    profile_comments = models.TextField(null=True, blank=True)
    profile_private_comments = models.TextField(null=True, blank=True)

    # Consent

    def __str__(self):
        return "{0}'s profile".format(self.user.username)


@receiver(post_save, sender=User)
def create_item(sender, instance, created, **kwargs):
    if created:
        profile = ProfileModel(user=instance)
        profile.save()
