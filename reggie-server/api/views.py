# ViewSets define the view behavior.
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from django.contrib.auth.models import User

from api import serializers
from registration import models


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def perform_create(self, serializer: serializers.UserSerializer):
        user: User = serializer.save()

        user.set_password(serializer.validated_data['password'])


class ConventionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ConventionModel.objects.all()
    serializer_class = serializers.ConventionSerializer

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        """
        List all conventions with theit opening and closing times
        Cached for 60 seconds
        """
        return super(ConventionViewSet, self).list(request, args, kwargs)


class RegistrationViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.RegistrationSerializer
    queryset = models.RegistrationModel.objects.all()

    def create(self, request, *args, **kwargs):
        now = timezone.now()
        serializer = serializers.RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        convention = serializer.validated_data.get('convention')

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
    def list(self, request, *args, **kwargs):
        return super(RegistrationAddonViewSet, self).list(request, args, kwargs)


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.PaymentSerializer
    queryset = models.PaymentModel.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    filterset_fields = ('registration', 'date_registered')
    ordering_fields = ('date_registered', 'amount')

    def get_queryset(self):
        return models.PaymentModel.objects.filter(registration__user=self.request.user)
