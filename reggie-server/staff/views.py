# Create your views here.
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

import registration.models
import staff.serializers


class StaffRegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Manage users registrations by accepting or rejecting them from the convention
    """
    serializer_class = staff.serializers.StaffRegistrationSerializer
    queryset = registration.models.RegistrationModel.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    filter_backends = (DjangoFilterBackend,)

    filterset_fields = ('convention', 'is_pending', 'is_accepted', 'user')

    @action(detail=True, methods=['GET', 'POST'])
    def accept(self, request, *args, **kwargs):
        registration = self.get_object()

        if request.method == 'POST':
            registration.is_accepted = True
            registration.is_pending = False

            registration.save()

        return Response(self.get_serializer(registration, many=False).data)

    @action(detail=True, methods=['GET', 'POST'])
    def reject(self, request, *args, **kwargs):
        registration = self.get_object()

        if request.method == 'POST':
            registration.is_accepted = False
            registration.is_pending = False

            registration.save()

        return Response(self.get_serializer(registration, many=False).data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = staff.serializers.UserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAdminUser,)

    def get_serializer_class(self):
        if self.action == 'warn':
            return staff.serializers.WarningSerializer
        elif self.action == 'ban':
            return staff.serializers.BanSerializer
        else:
            return staff.serializers.UserSerializer

    @action(detail=True, methods=['get', 'post'])
    def warn(self, request, *args, **kwargs):
        warnings = self.get_object().warnings

        if request.method == 'POST':
            warning_serializer = self.get_serializer(data=request.data)
            if warning_serializer.is_valid(raise_exception=True):
                warning_serializer.save()

        return Response(self.get_serializer(warnings, many=True).data)

    @action(detail=True, methods=['get', 'post'])
    def ban(self, request, *args, **kwargs):
        bans = self.get_object().bans

        if request.method == 'POST':
            ban_serializer = self.get_serializer(data=request.data)
            if ban_serializer.is_valid(raise_exception=True):
                ban_serializer.save()

        return Response(self.get_serializer(bans, many=True).data)
