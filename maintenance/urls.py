from django.urls import path
from .views import MaintenanceListView, MaintenanceAddView, MaintenanceDeleteView, MaintenanceUpdateView, MaintenanceDetailView

from . import views

#Specifies the URL patterns to use after the initial requst is routed using the master url list for all apps.
urlpatterns=[    
    path("", MaintenanceListView.as_view(), name="maintenance_listing"),
    path("<int:pk>/", MaintenanceDetailView.as_view(), name="maintenance_detail"),
    path("add/", MaintenanceAddView.as_view(), name="maintenance_add"),
    path("<int:pk>/update/", MaintenanceUpdateView.as_view(), name="maintenance_update"),
    path("<int:pk>/delete/", MaintenanceDeleteView.as_view(), name="maintenance_delete")
    ]