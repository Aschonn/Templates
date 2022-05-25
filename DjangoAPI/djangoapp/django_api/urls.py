from rest_framework import routers
from django.urls import include, path
from django_api.views import TeamsViewSet

router = routers.DefaultRouter()
router.register(r'teams', TeamsViewSet)

urlpatterns = [
   path('', include(router.urls)),
]

