from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import login, logout
from app.models import Problema
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^problemi/$', views.problemi, name='problemi'),
    url(r'^(?P<problema_id>[0-9]+)/problema_edit/$', views.problema_edit, name='problema_edit'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^info/$', views.info, name='info'),
    url(r'^pdf/(?P<yearstart>[0-9]{4})/(?P<monthstart>[0-9]{2})/(?P<daystart>[0-9]{2})/(?P<yearend>[0-9]{4})/(?P<monthend>[0-9]{2})/(?P<dayend>[0-9]{2})/$', views.pdf),
    url(r'^pdf/(?P<yearstart>[0-9])/(?P<monthstart>[0-9])/(?P<daystart>[0-9])/(?P<yearend>[0-9])/(?P<monthend>[0-9])/(?P<dayend>[0-9])/$', views.pdf),
    url(r'^getpdf/$', views.getpdf),
    url(r'^getall/$', views.getall),
    ]
