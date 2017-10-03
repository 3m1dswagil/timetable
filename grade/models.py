# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Disciplina(models.Model):
    disciplina = models.CharField(max_length=50)
    cod_disc = models.CharField(max_length=50)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here.
