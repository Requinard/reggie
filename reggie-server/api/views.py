# ViewSets define the view behavior.
from django.core.cache import cache
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response

import api.permissions
import bookings.models
import payments.models
import users.models
from api import serializers
from registration import models


class ConventionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ConventionModel.objects.filter(is_public=True)
    serializer_class = serializers.ConventionSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.RegistrationSerializer
    queryset = models.RegistrationModel.objects.all()

    def create(self, request, *args, **kwargs):
        now = timezone.now()
        serializer = serializers.RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        convention = cache.get_or_set(request.data['convention'], serializer.validated_data.get('convention'))

        if now <= convention.con_reg_start_time:
            return Response("The convention registration has not yet opened.", status=status.HTTP_406_NOT_ACCEPTABLE)
        elif now > convention.con_reg_close_time:
            return Response("The convention registration has closed.", status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return super(RegistrationViewSet, self).create(request, args, kwargs)

    def update(self, *args, **kwargs):
        return Response("You are not allowed to edit your registration. Please contact a staffer.",
                        status=status.HTTP_403_FORBIDDEN)

    def partial_update(self, request, *args, **kwargs):
        return Response("You are not allowed to partially edit your registration. Please contact a staffer.",
                        status=status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        """
        Make sure that a user can only get his or her own registrations
        """
        return models.RegistrationModel.objects.filter(user=self.request.user)

    def perform_create(self, serializer: serializers.RegistrationSerializer):
        serializer.save(user=self.request.user)


class RegistrationAddonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.RegistrationAddinModel.objects.all()
    serializer_class = serializers.RegistrationAddonSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationAddonViewSet, self).dispatch(request, args, kwargs)


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.PaymentSerializer
    queryset = payments.models.PaymentModel.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    filterset_fields = ('registration', 'date_registered')
    ordering_fields = ('date_registered', 'amount')

    def get_queryset(self):
        return models.PaymentModel.objects.filter(registration__user=self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, api.permissions.ProfileEditPermissions)
    queryset = users.models.ProfileModel.objects.filter()
    serializer_class = serializers.ProfileSerializer

    @action(detail=False, methods=['get', ])
    def me(self, *args, **kwargs):
        profile = self.request.user.profile
        serializer = self.get_serializer(profile, many=False)
        return Response(serializer.data)


class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = bookings.models.HotelModel.objects.filter(is_public=True)
    serializer_class = serializers.HotelSerializer


class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = bookings.models.RoomModel.objects.filter(is_public=True)
    serializer_class = serializers.RoomSerializer

    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('hotel', 'is_locked')
