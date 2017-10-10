# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Disciplina
from .models import Professor
from .models import Aula


admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Aula)

# Register your models here.
