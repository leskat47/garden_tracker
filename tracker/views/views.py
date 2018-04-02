from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView, UpdateView
from tracker import forms
from django.urls import reverse_lazy

from tracker.models import Garden, Log, Location, Planting, Plant, Status


class GardenView(generic.TemplateView):
    """ Main Page """
    template_name = "tracker/garden_list.html"

    def get_context_data(self, **kwargs):
        context = super(GardenView, self).get_context_data(**kwargs)
        context['logs'] = Log.objects.all()
        context['garden'] = Garden.objects.get(id=1)
        live_plants = list(map(lambda s: s.id, Status.objects.exclude(status='dead').all()))
        context['plants'] = Plant.objects.filter(planting__status__in=live_plants).order_by('name').distinct()
        return context


class LocationsView(generic.ListView):
    template_name = 'tracker/locations.html'
    model = Location

    def get_context_data(self, **kwargs):
        context = super(LocationsView, self).get_context_data(**kwargs)
        # import pdb; pdb.set_trace()
        return context


class LocationUpdateView(UpdateView):
    model = Location
    fields = ['name', 'exposure', 'description']
    template_name_suffix = '_update_form'

    success_url = reverse_lazy('settings')


class PlantView(generic.ListView):
    """ Show list of current plant plantings and their status """

    template_name ='tracker/plants.html'
    # queryset = Plant.objects.order_by("name").prefetch_related('planting_set')
    queryset = Plant.objects.order_by("name")


class PlantDetailView(generic.DetailView):
    """ Show data about a particular species of plant """
    model = Plant

    queryset = Plant.objects.prefetch_related('planting_set')


class LogView(generic.ListView):
    # model = Log
    template_name = "tracker/logs.html"

    queryset = Log.objects.order_by("-date")


class CreateLogView(FormView):
    model = Log
    template_name = "tracker/update_form.html"
    success_url = '/tracker/log/'
    form_class = forms.LogForm

    def form_valid(self, form):
        log = Log(notes=form.cleaned_data['notes'], date=form.cleaned_data['date'])
        log.save()

        log.area.add(form.cleaned_data['area'].first().id)
        log.save()

        return super(CreateLogView, self).form_valid(form)
