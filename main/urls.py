from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('testform/', include('testform.urls')),
    path('contacts', include('contacts.urls')),    
]