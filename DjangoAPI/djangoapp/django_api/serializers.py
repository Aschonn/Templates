'''
    Why Serializers? 

        - Convert the Teams model into DJSON that will be used by the API to return the data to the user

'''

from rest_framework import serializers
from django_api.models import Teams

class TeamsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Teams
       fields = ('name', "sport")

