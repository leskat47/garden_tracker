from django.shortcuts import render
from django.views import generic

from .models import Garden, Log, Location


class GardenView(generic.ListView):
    model = Garden
    template_name = "tracker/garden_list.html"

class LogView(generic.ListView):
    model = Log
    template_name = "tracker/logs.html"
