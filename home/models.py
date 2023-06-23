from django.db import models

# Create your models here.
class UserLocation(models.Model):
    location = models.CharField(max_length=100)