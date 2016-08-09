from django.conf.urls import url
from django.contrib import admin
from .views import home, weatherAPI

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^current/$', weatherAPI, name='weatherapi'),
]