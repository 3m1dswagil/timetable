# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import DiscForm

# Create your views here.

def disc_new(request):
    form = DiscForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'grade/cad_disc.html', {'form': form})
