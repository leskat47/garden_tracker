from django.shortcuts import render
from django.views import generic

from .models import Garden, Log, Location, Planting, Plant


class GardenView(generic.TemplateView):
    """ Main Page """
    template_name = "tracker/garden_list.html"

    def get_context_data(self, **kwargs):
        context = super(GardenView, self).get_context_data(**kwargs)
        context['logs'] = Log.objects.all()
        context['garden'] = Garden.objects.get(id=1)
        return context

class PlantView(generic.ListView):
    """ Show list of current plant plantings and their status """

    template_name ='tracker/plant_list.html'

    queryset = Plant.objects.order_by("name")


class LogView(generic.ListView):
    # model = Log
    template_name = "tracker/logs.html"

    queryset = Log.objects.order_by("-date")


# class PlantView(generic.ListView):
#     template_name = "tracker/plants.html"
