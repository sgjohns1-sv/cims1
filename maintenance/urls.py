from django.urls import path

from . import views

urlpatterns=[    
    path("", views.index, name="maintenance"),
    path("/add/", views.add, name="add"),
    ]