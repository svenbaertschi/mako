from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.weather, name='weather'),
    url(r'^weather.html$', views.weather, name='weather'),
]
