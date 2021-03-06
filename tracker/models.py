from __future__ import unicode_literals

from django.db import models
from datetime import date
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Fixed values ##############################################################
class Status(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Exposure(models.Model):
    exposure_type = models.CharField(max_length=20)

    def __str__(self):
        return self.exposure_type


class Soil(models.Model):
    soil_type = models.CharField(max_length=20)

    def __str__(self):
        return self.soil_type


# Garden data #################################################################
class Garden(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=70)
    sci_name = models.CharField(max_length=70)
    height = models.IntegerField()
    width = models.IntegerField()
    color = models.CharField(max_length=20)
    exposure = models.ManyToManyField(Exposure)
    moisture = models.CharField(max_length=25)
    bloom_season = models.CharField(max_length=25)
    food = models.CharField(max_length=20, null=True)
    soil = models.ManyToManyField(Soil)
    notes = models.TextField(null=True)

    def plantings(self):
        return Planting.objects.filter(plant=self).exclude(status__status='dead')

    def get_absolute_url(self):
        """URL."""

        return reverse('plant-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=20)
    exposure = models.ManyToManyField(Exposure)
    description = models.CharField(max_length=25)
    garden = models.ForeignKey(Garden)
    plants = models.ManyToManyField(Plant, through='Planting')

    def get_absolute_url(self):
        """Update URL."""

        return reverse('location', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Location %s>" % self.name


class Planting(models.Model):
    date = models.DateField(default=date.today)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True)
    status = models.ForeignKey(Status)
    description = models.TextField(null=True)

    def __str__(self):
        return "<%s planted on %s>" % (self.plant, self.date)


# Logs ########################################################################
class Log(models.Model):
    area = models.ManyToManyField(Location)
    notes = models.TextField()
    date = models.DateField(default=date.today)

    def plantingnotes(self):
        return PlantingNote.objects.filter(log=self)

    def newplanting(self):
        return Planting.objects.filter(date=self.date)

    # def __str__(self):
    #     return "%s on %s" % (self.area, self.date)

class PlantingNote(models.Model):
    note = models.TextField()
    planting = models.ForeignKey(Planting)
    log = models.ForeignKey(Log)

    def __str__(self):
        return "<Planting note on %s>" % (self.planting.plant.name)
