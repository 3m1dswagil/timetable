from django.conf.urls import url
from . import views


urlpatterns = [
url(r'^d', views.disc_new, name='disc_new'),
url(r'^p', views.prof_new, name='prof_new'),
url(r'^$', views.aula_new, name='aula_new'),

]
