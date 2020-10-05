from django.contrib import admin
from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^signin/$', views.login),
    url(r'^signup/$', views.register),
    
]

