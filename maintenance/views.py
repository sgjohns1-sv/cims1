from django.urls import reverse_lazy
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
    fields = ["asset", "title", "description", "cost", "date"]

class MaintenanceUpdateView(UpdateView):
    template_name="maintenance/updateview.html"
    model=Maintenance
    fields = ["asset", "title", "description", "cost", "date"]

class MaintenanceDeleteView(DeleteView):
    template_name="maintenance/deleteview.html"
    model=Maintenance
    success_url = reverse_lazy("maintenance_list")