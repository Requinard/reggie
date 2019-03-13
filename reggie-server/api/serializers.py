# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers

from registration import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ConventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ConventionModel
        fields = ('url', 'name', 'con_start_time', 'con_reg_time', 'price')


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RegistrationModel
        fields = ('url', 'user', 'is_pending', 'is_accepted', 'addons', 'payments')
        read_only_fields = ('payments',)


class RegistrationAddonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RegistrationAddinModel
        fields = ('url', 'name', 'description', 'price')


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PaymentModel
        fields = ('url', 'registration', 'amount', 'date_registered', 'notes')
