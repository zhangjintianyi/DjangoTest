from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$', views.log_in, name='login'),
    url('^thanks$', views.thank_reg, name='thanks'),

]
