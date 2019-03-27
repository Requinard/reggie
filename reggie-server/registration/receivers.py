from django.core.mail.message import EmailMessage
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from registration.models import RegistrationModel, RegistrationAddinModel


@receiver(post_save, sender=RegistrationModel)
def post_save(sender, instance: RegistrationModel, created, *args, **kwargs):
    email = EmailMessage(
        subject="Your registration for {0} has been received".format(instance.convention.name),
        body="Your registration has been received and is now pending! You will be manually approved!",
        to=instance.user.email
    ) if created else EmailMessage(
        subject="Your registration for {0} has been altered!".format(instance.convention.name),
        body="Your regisration has been altered, you can check the website for the newly updated data",
        to=instance.user.email
    )

    email.send(fail_silently=False)


@receiver(post_save, sender=RegistrationAddinModel)
def registration_addin_notification(sender, instance: RegistrationAddinModel, created, *args, **kwargs):
    if created:
        EmailMessage(
            subject="An addin has been added to your account!",
            body="{0} has been added to your registration for {1}".format(instance.name, instance.convention.name)
        )
