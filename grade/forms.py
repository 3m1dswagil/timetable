# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Disciplina
from .models import Professor
from .models import Aula




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
class ProfForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ['Nome', 'disciplinas']
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'João da Silva'}),
            'disciplinas': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Matematica'}),
        }

        error_messages = {
            'Nome':{
                'required': 'Este campo é obrigatório'
            },
            'disciplinas':{
                'required': 'Este campo é obrigatório'
            },
        }
class AulaForm(forms.ModelForm):

    class Meta:
        model = Aula
        fields = ['NomeProf', 'email']
        widgets = {
            'NomeProf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'José da Silva'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': '@gmail'}),
        }

        error_messages = {
            'NomeProf':{
                'required': 'Este campo é obrigatório'
            },
            'email':{
                'required': 'Este campo é obrigatório'
            },
        }
