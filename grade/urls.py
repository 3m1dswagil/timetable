from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^novadisciplina', views.disciplina_new, name='disciplina_new'),
    url(r'^disciplinas', views.disciplina_list, name='disciplina_list'),
    url(r'^novoprofessor', views.professor_new, name='professor_new'),
    url(r'^professores', views.professor_list, name='professor_list'),
    url(r'^novaturma', views.turma_new, name='turma_new'),
    # url(r'^disciplinaministrada', views.disciplina_ministrada_new, name='disciplina_ministrada_new'),
    url(r'^turma', views.turma_list, name='turma_list'),
    url(r'^$', views.pagina_inicial, name='pagina_inicial'),

]
