from __future__ import unicode_literals

from django.db import models


# Fixed values
class Status(models.Model):
    status = models.CharField(max_length=20)


class Exposure(models.Model):
    exposure_type = models.CharField(max_length=20)


class Soil(models.Model):
    soil_type = models.CharField(max_length=20)


class Garden(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)


class Location(models.Model):
    name = models.CharField(max_length=20)
    exposure = models.ManyToManyField(Exposure)
    description = models.CharField(max_length=25)
    location = models.ForeignKey(Garden)


class Plant(models.Model):
    name = models.CharField(max_length=70)
    sci_name = models.CharField(max_length=70)
    height = models.IntegerField()
    width = models.IntegerField()
    color = models.CharField(max_length=20)
    exposure = models.ManyToManyField(Exposure)
    moisture = models.CharField(max_length=25)
    bloom_season = models.CharField(max_length=25)
    food = models.BooleanField()
    soil = models.ManyToManyField(Soil)


class Planting(models.Model):
    date = models.DateField()
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)
    status = models.ForeignKey(Status)


class Log(models.Model):
    area = models.ManyToManyField(Location)
    notes = models.TextField()


class PlantingNotes(models.Model):
    note = models.TextField()
    planting = models.ForeignKey(Planting)
    log = models.ForeignKey(Log)
