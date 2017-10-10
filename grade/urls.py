from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.disc_new, name='disc_new'),
    url(r'^cadastradas', views.discp_cad, name='disc_cad'),

]
