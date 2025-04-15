from .models import Asset
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404


# Create your views here.

class AssetListView(ListView):
    template_name = "assets/index.html"
    model = Asset

class AssetDetailView(DetailView):
    template_name = "assets/viewasset.html"
    model = Asset
    def get_queryset(self):
        self.asset = get_object_or_404(Asset, id=self.kwargs["pk"])
        print(self.asset.id)
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
    success_url="assets/"
