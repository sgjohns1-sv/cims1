from django.urls import path
from .views import MaintenanceAddView

from . import views

urlpatterns=[    
    path("", views.index, name="maintenance"),
    path("add/", MaintenanceAddView.as_view()),
    ]