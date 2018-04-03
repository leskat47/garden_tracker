from django.conf.urls import url, include
from views import views

urlpatterns = [

    url(r'^garden/$', views.GardenView.as_view(), name='garden'),
    url(r'^settings/$', views.LocationsView.as_view(), name="settings"),
    url(r'^location_update/(?P<pk>\d+)$', views.LocationUpdateView.as_view(), name='location'),
    url(r'^log/$', views.LogView.as_view(), name='log'),
    url(r'^plants/$', views.PlantView.as_view(), name='plants'),
    url(r'^update/$', views.CreateLogView.as_view(), name='update'),
    url(r'^plant/(?P<pk>\d+)$', views.PlantDetailView.as_view(), name='plant-detail'),
    url(r'^plant_new/$', views.CreatePlantView.as_view(), name='plant-new'),
    url(r'^planting_new/$', views.CreatePlantingView.as_view(), name='planting-new'),    

    url(r'^accounts/', include('django.contrib.auth.urls')),

]
