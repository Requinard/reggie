# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers

import bookings.models
import payments.models
import users.models
from registration import models


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ConventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ConventionModel
        fields = (
            'url', 'name', 'con_event_start_date', 'con_event_close_date', 'con_reg_start_time', 'con_reg_close_time',
            'price')


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RegistrationModel
        fields = ('url', 'convention', 'user', 'is_pending', 'is_accepted', 'addons', 'payments', 'get_badge_number')
        read_only_fields = ('payments', 'user', 'is_accepted', 'is_pending', 'payments', 'addons')


class RegistrationAddonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RegistrationAddinModel
        fields = ('url', 'name', 'description', 'price')


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = payments.models.PaymentModel
        fields = ('url', 'registration', 'amount', 'date_registered', 'notes')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = users.models.ProfileModel
        fields = (
            'url', 'user', 'is_private_profile', 'address_street', 'address_postal_code', 'address_number',
            'address_city', 'address_country', 'date_of_birth', 'gender', 'phone_number', 'shirt_size',
            'profile_comments')
        read_only_fields = ('user',)


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookings.models.HotelModel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookings.models.RoomModel
        fields = '__all__'
