from django.urls import path
from .views import MaintenanceListView, MaintenanceAddView, MaintenanceDetailView

from . import views

urlpatterns=[    
    path("", MaintenanceListView.as_view(), name="maintenance_list"),
    path("<int:pk>", MaintenanceDetailView.as_view(), name="maintainence_detail"),
    path("add/", MaintenanceAddView.as_view(), name="maintenance_add"),
    ]