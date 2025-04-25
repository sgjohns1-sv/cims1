from django.shortcuts import render
from .models import Maintenance
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

class MaintenanceListView(ListView):
    template_name="maintenance/index.html"
    model = Maintenance

class MaintenanceDetailView(DetailView):
    template_name="maintenance/detailview.html"
    model = Maintenance

class MaintenanceAddView(CreateView):
    template_name="maintenance/addview.html"
    model = Maintenance
    fields = ["maint_assetID", "maint_title", "maint_description", "maint_cost", "maint_date"]

class MaintenanceUpdateView(UpdateView):
    template_name="maintenance/updateview.html"
    model=Maintenance
    fields = ["maint_assetID", "maint_title", "maint_description", "maint_cost", "maint_date"]
