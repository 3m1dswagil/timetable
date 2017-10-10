# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import DiscForm
from .forms import ProfForm
from .forms import AulaForm

# Create your views here.

def disc_new(request):
    form = DiscForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'grade/cad_disc.html', {'form': form})
def prof_new(request):
    form = ProfForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'grade/cad_prof.html', {'form': form})
def aula_new(request):
    form = AulaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'grade/aula.html', {'form': form})
