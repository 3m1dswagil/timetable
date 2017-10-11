from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^novadisciplina', views.disc_new, name='disc_new'),
    url(r'^disciplinas', views.disc_list, name='disc_list'),
    url(r'^novoprofessor', views.prof_new, name='prof_new'),

]
