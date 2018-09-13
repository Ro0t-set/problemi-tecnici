from django import forms
from django.db import models
from django.forms import formset_factory
from django.utils import timezone
import re
from django.forms import BaseModelFormSet
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Aula,Problema


class PubbicaProblema(forms.ModelForm):
    class Meta:
        model = Problema
        fields = ['classe','descrizioneProblema']
