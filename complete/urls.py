from django.conf.urls import include, url
from django.contrib import admin
from complete import views
from . import views

urlpatterns = [
    url(r'^$', views.index , name="index"),
]
