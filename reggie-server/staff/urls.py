from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from staff.views import StaffRegistrationViewSet, UserViewSet

router = DefaultRouter()
router.register('registrations', StaffRegistrationViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
