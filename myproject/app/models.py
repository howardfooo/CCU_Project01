from django.db import models
from mapbox_location_field.models import LocationField

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = LocationField()
# Create your models here.
