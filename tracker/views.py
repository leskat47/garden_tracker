from django.shortcuts import render
from django.views import generic

from .models import Garden, Location

class GardenView(generic.ListView):
    model = Garden
    template_name = "tracker/garden_list.html"
