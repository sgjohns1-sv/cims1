from .models import Asset
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

class AssetListView(ListView):
    template_name = "assets/index.html"
    model = Asset
    def get_queryset(self):
        if ('search' not in self.request.GET.keys()):
            asset_list = Asset.objects.all()
        else:
            asset_list = Asset.objects.filter(Q(asset_manufacturer__icontains=self.request.GET['search']) | Q(asset_model__icontains=self.request.GET['search']) | Q(asset_location__icontains=self.request.GET['search']) | Q(asset_sn__icontains=self.request.GET['search']) | Q(asset_cost__icontains=self.request.GET['search']) | Q(asset_purchaseDate__icontains=self.request.GET['search']) | Q(asset_eolDate__icontains=self.request.GET['search']) | Q(asset_notes__icontains=self.request.GET['search']))
        return asset_list
    
class AssetDetailView(DetailView):
    template_name = "assets/viewasset.html"
    model = Asset
    def get_queryset(self):
        self.asset = get_object_or_404(Asset, id=self.kwargs["pk"])
        return Asset.objects.filter(id=self.asset.id)

class AssetAddView(CreateView):
    template_name="assets/newasset.html"
    model = Asset
    fields = ["manufacturer", "model", "sn", "location", "cost", "purchase_date", "eol_date", "notes"]

class AssetUpdateView(UpdateView):
    template_name="assets/updateasset.html"
    model = Asset
    fields = ["manufacturer", "model", "sn", "location", "cost", "purchase_date", "eol_date", "notes"]

class AssetDeleteView(DeleteView):
    template_name="assets/deleteasset.html"
    model = Asset
    success_url = reverse_lazy("asset_assets")
