# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Aula(models.Model):
    aule= models.CharField(max_length=100, default="")
    def __str__(self):
        return str(self.aule)

    class Meta:
        verbose_name = "Aula"
        verbose_name_plural = "Aule"

class Problema(models.Model):
    autore = models.ForeignKey('auth.User')
    classe = models.ForeignKey('Aula')
    descrizioneProblema = models.TextField(max_length=1000, default="")
    note = models.TextField(blank=True)
    risoluzione=  models.IntegerField(default=0)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.autore)
