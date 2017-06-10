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

class PlantView(generic.TemplateView):
    """ Show list of current plant plantings and their status """

    # pl = Plant.objects.all()
    # print pl[0].objects
    # qset = Planting.objects.select_related('plant') \
    #                             .select_related('status') \
    #                             .exclude(status__status='dead')
    template_name ='tracker/planting_list.html'

    def get_context_data(self, **kwargs):
        """ {'plants': {'pansy': [<planting>, <planting>], ...}} """
        context = super(PlantView, self).get_context_data(**kwargs)
        plantings = Planting.objects.select_related('plant') \
                                    .select_related('status') \
                                    .exclude(status__status='dead').all()
        context['plants'] = {}
        for plant in plantings:
            print plant
            context['plants'].setdefault(plant.plant.name, []).append(plant)
        print context['plants']['Geranium'][0].location
        return context


class LogView(generic.ListView):
    # model = Log
    template_name = "tracker/logs.html"

    queryset = Log.objects.order_by("-date")


# class PlantView(generic.ListView):
#     template_name = "tracker/plants.html"
