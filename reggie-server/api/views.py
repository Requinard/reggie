# ViewSets define the view behavior.
from django.contrib.auth.models import User
from rest_framework import viewsets

from api import serializers
from registration import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ConventionViewSet(viewsets.ModelViewSet):
    queryset = models.ConventionModel.objects.all()
    serializer_class = serializers.ConventionSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = models.RegistrationModel.objects.all()
    serializer_class = serializers.RegistrationSerializer


class RegistrationAddonViewSet(viewsets.ModelViewSet):
    queryset = models.RegistrationAddinModel.objects.all()
    serializer_class = serializers.RegistrationAddonSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = models.PaymentModel.objects.filter()
    serializer_class = serializers.PaymentSerializer

