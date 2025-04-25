from django.shortcuts import render
from .models import Maintenance
from django.views.generic import ListView, CreateView

# Create your views here.

class MaintenanceListView(ListView):
    template_name="maintenance/index.html"
    model = Maintenance

class MaintenanceAddView(CreateView):
    template_name="assets/newasset.html"
    model = Maintenance
    fields = ["maint_assetID", "maint_title", "maint_description", "maint_cost", "maint_date"]