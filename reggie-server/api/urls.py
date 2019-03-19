from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter(trailing_slash=True)
router.register(r'users', views.UserViewSet)
router.register(r'conventions', views.ConventionViewSet)
router.register(r'registrations', views.RegistrationViewSet)
router.register(r'addons', views.RegistrationAddonViewSet)
router.register(r'payments', views.PaymentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
