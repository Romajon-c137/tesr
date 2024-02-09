
from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .view import ResultViewSet, LabAPIView

router = routers.DefaultRouter()
router.register('results', ResultViewSet, 'results')

urlpatterns = [
    path("", include(router.urls), name='api'),
    path("neworder/", LabAPIView.as_view(), name='neworder'),
]