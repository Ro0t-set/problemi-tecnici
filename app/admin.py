# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Aula, Problema

admin.site.register(Aula)
admin.site.register(Problema)
