from django.db import models

class Teams(models.Model):
   name = models.CharField(max_length=100)
   sport = models.CharField(max_length=100)
