# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import DiscForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import ProfForm
from .forms import AulaForm
from django.views.generic import ListView
from grade.models import Disciplina
from django.template.response import TemplateResponse


# Create your views here.

def disc_new(request):
    form = DiscForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'grade/cad_disc.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                   password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated', successfully)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request, 'sua-app/login.html', {'form': form})

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

def discp_cad(request):
    data = Disciplina.objects.all()
    return TemplateResponse(request, 'grade/lista_disc.html', {'data': data})
