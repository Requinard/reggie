from django.contrib.auth.models import User
from rest_framework import serializers

import registration.models
import users.models


class WarningSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = users.models.WarningModel


class BanSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = users.models.BanModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    warnings = WarningSerializer(many=True)
    bans = BanSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'warnings', 'bans')
        read_only_fields = ('username', 'email', 'warnings', 'bans')


class StaffRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer specifically made for staff
    """
    user = UserSerializer(many=False)

    class Meta:
        model = registration.models.RegistrationModel
        fields = ('convention', 'url', 'is_pending', 'is_accepted', 'get_badge_number', 'user')
        read_only_fields = ('convention', 'uuid', 'get_badge_number', 'user')
