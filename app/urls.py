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
    ]
