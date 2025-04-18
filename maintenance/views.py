from django.shortcuts import render
from .models import Maintenance
from django.views.generic import CreateView

# Create your views here.

def index(request):
    allMaintenance = Maintenance.objects.all()
    context = {"allMaintenance": allMaintenance}
    return render(request, "maintenance/index.html", context)

class MaintenanceAddView(CreateView):
    template_name="assets/newasset.html"
    model = Maintenance
    fields = ["maint_assetID", "maint_title", "maint_description", "maint_cost", "maint_date"]