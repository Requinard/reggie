# Serializers define the API representation.
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers

from registration import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'is_superuser', 'password')
        read_only_fields = ('is_staff', 'is_superuser')


class ConventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ConventionModel
        fields = (
            'url', 'name', 'con_event_start_date', 'con_event_close_date', 'con_reg_start_time', 'con_reg_close_time',
            'price')


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RegistrationModel
        fields = ('url', 'convention', 'user', 'is_pending', 'is_accepted', 'addons', 'payments')
        read_only_fields = ('payments', 'user', 'is_accepted', 'is_pending', 'payments')


class RegistrationAddonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RegistrationAddinModel
        fields = ('url', 'name', 'description', 'price')


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PaymentModel
        fields = ('url', 'registration', 'amount', 'date_registered', 'notes')
