from .models import Asset
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404, get_list_or_404


# Create your views here.

class AssetListView(ListView):
    template_name = "assets/index.html"
    model = Asset

    def get_queryset(self):
        if (self.request.GET['search'] == ''):
            print('here1')
            asset_list = Asset.objects.all()
        else:
            print("here")
            asset_list = Asset.objects.filter(asset_manufacturer__icontains=self.request.GET['search'])
        return asset_list
    

class AssetSearchView(ListView):
    template_name="index.html"
    model = Asset
    
class AssetDetailView(DetailView):
    template_name = "assets/viewasset.html"
    model = Asset
    def get_queryset(self):
        self.asset = get_object_or_404(Asset, id=self.kwargs["pk"])
        return Asset.objects.filter(id=self.asset.id)

class AssetAddView(CreateView):
    template_name="assets/newasset.html"
    model = Asset
    fields = ["asset_manufacturer", "asset_model", "asset_sn", "asset_location", "asset_cost", "asset_purchaseDate", "asset_eolDate", "asset_notes"]

class AssetUpdateView(UpdateView):
    template_name="assets/updateasset.html"
    model = Asset
    fields = ["asset_manufacturer", "asset_model", "asset_sn", "asset_location", "asset_cost", "asset_purchaseDate", "asset_eolDate", "asset_notes"]

class AssetDeleteView(DeleteView):
    template_name="assets/deleteasset.html"
    model = Asset
    success_url = reverse_lazy("asset_assets")
