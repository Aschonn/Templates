'''
    Routes and API URLS:

        - After the serializers are created we need to create a view to the API and connect it to the Django URLs.
        - Viewsets provide the advantage of combining multiple sets of logic into a single class.


'''

from rest_framework import viewsets

from django_api.serializers import TeamsSerializer
from django_api.models import Teams


# Create your views here.


class TeamsViewSet(viewsets.ModelViewSet):
   queryset = Teams.objects.all()
   serializer_class = TeamsSerializer
