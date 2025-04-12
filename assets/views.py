from django.shortcuts import render
from .models import Asset

# Create your views here.

def index(request):
    allAssets = Asset.objects.all()
    context = {"allAssets": allAssets}
    return render(request, "assets/index.html", context)
def view(request):
    return render(request, "assets/viewasset.html")
def add(request):
    return render(request, "assets/newasset.html")