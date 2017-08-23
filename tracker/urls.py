from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^garden/$', views.GardenView.as_view(), name='garden'),
    url(r'^settings/$', views.LocationsView.as_view(), name="settings"),
    url(r'^log/$', views.LogView.as_view(), name='log'),
    url(r'^plants/$', views.PlantView.as_view(), name='plants'),
    url(r'^update/$', views.CreateLogView.as_view(), name='update'),
    url(r'^plant/(?P<pk>\d+)$', views.PlantDetailView.as_view(), name='plant-detail'),
]
