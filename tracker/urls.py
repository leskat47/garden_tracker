from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^garden/$', views.GardenView.as_view(), name='garden'),
    url(r'^log/$', views.LogView.as_view(), name='log'),
    url(r'^plants/$', views.PlantView.as_view(), name='plants'),
    url(r'^update/$', views.CreateLogView.as_view(), name='update'),
    # url(r'^newlog/$', views.NewLogView.as_view(), name='newlog'),
    # url(r'^updatelog/$', views.update, name='updatelog'),
]
