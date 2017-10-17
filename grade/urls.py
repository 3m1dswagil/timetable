from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^novadisciplina', views.disc_new, name='disc_new'),
    url(r'^disciplinas', views.disc_list, name='disc_list'),
    url(r'^novoprofessor', views.prof_new, name='prof_new'),
    url(r'^professores', views.prof_list, name='prof_list'),
    url(r'^novaturma', views.turma_new, name='turma_new'),
    url(r'^turmas', views.turma_list, name='turma_list'),
    url(r'^$', views.pag_incial, name='pag_incial'),

]
