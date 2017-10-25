# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Disciplina
from .models import Professor
from .models import Turma

class DiscForm(forms.ModelForm):

    class Meta:
        model = Disciplina
        fields = ['cod_disc', 'disciplina']
        widgets = {
            'cod_disc': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '123matematica123'}),
            'disciplina': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': 'Matematica'}),
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
        fields = ['nome', 'cod_prof', 'disc_p']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome do professor'}),
            'cod_prof': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': '123prof123'}),

            }

        error_messages = {
            'nome':{
                'required': 'Este campo é obrigatório'
            },
            'cod_prof':{
                'required': 'Este campo é obrigatório'
            },
        }

class TurmaForm(forms.ModelForm):

    class Meta:
        model = Turma
        fields = ['cod_turma', 'turma']
        widgets = {
            'cod_turma': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '3m1'}),
            'turma': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': '3m1'}),
        }

        error_messages = {
            'turma':{
                'required': 'Este campo é obrigatório'
            },
            'cod_turma':{
                'required': 'Este campo é obrigatório'
            },
        }
