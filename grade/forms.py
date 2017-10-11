# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Disciplina
from django.contrib.auth.models import User

class DiscForm(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ['cod_disc', 'disciplina']
        widgets = {
            'cod_disc': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': '123matematica123'}),
            'disciplina': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Matematica'}),
        }

        error_messages = {
            'disciplina':{
                'required': 'Este campo é obrigatório'
            },
            'cod_disc':{
                'required': 'Este campo é obrigatório'
            },
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
