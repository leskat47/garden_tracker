from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^garden/$', views.GardenView.as_view(), name='garden'),
    url(r'^log/$', views.LogView.as_view(), name='log'),
]