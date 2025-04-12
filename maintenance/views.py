from django.shortcuts import render
from .models import Maintenance

# Create your views here.

def index(request):
    allMaintenance = Maintenance.objects.all()
    context = {"allMaintenance": allMaintenance}
    return render(request, "maintenance/index.html", context)
def add(request):
    return render(request, "maintenance/add.html")