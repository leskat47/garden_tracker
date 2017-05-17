from __future__ import unicode_literals

from django.db import models


class Plant(models.Model):
    name = models.CharField(max_length="70")
    sci_name = models.CharField(max_length="70")
    height = models.IntegerField()
    width = models.IntegerField()
    color = models.CharField(max_length="20")
    exposure = models.CharField(max_length="25")
    moisture = models.CharField(max_length="25")
    bloom_season = models.CharField(max_length="25")
    food = models.BooleanField()
