from django.urls import path
from .views import MaintenanceListView, MaintenanceAddView

from . import views

urlpatterns=[    
    path("", MaintenanceListView.as_view(), name="maintenance_list"),
    path("add/", MaintenanceAddView.as_view(), name="maintenance_add"),
    ]