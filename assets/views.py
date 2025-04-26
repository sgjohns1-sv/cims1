from .models import Asset
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.db.models import Q

#Class based view to display a list of Assets available.
class AssetListView(ListView):
    template_name = "assets/index.html" #Template used to render the list of assets.
    model = Asset #Specifies model to be used.
    def get_queryset(self):
        #If statement checks to see if the search query exists in the request data.
        if ('search' not in self.request.GET.keys()): #If it doesn't then the whole list of assets is returned as normal.
            asset_list = Asset.objects.all()
        else: #If it does, the objects are filtered based on this search query.
            asset_list = Asset.objects.filter(Q(asset_manufacturer__icontains=self.request.GET['search']) | Q(asset_model__icontains=self.request.GET['search']) | Q(asset_location__icontains=self.request.GET['search']) | Q(asset_sn__icontains=self.request.GET['search']) | Q(asset_cost__icontains=self.request.GET['search']) | Q(asset_purchaseDate__icontains=self.request.GET['search']) | Q(asset_eolDate__icontains=self.request.GET['search']) | Q(asset_notes__icontains=self.request.GET['search']))
        return asset_list
    
#Class based detail view used to show the details of an asset.
class AssetDetailView(DetailView):
    template_name = "assets/viewasset.html" #Specifies the template to use when rendering the model details.
    model = Asset
    def get_queryset(self): #Method that gets the Asset object specified to view and returns the Asset object to the page.
        self.asset = get_object_or_404(Asset, id=self.kwargs["pk"])
        return Asset.objects.filter(id=self.asset.id)

#Class based view used to add an object to the Asset model.
class AssetAddView(CreateView):
    template_name="assets/newasset.html" #Specifies the template to use when rendering the add asset form.
    model = Asset #Specifies the model to use.
    fields = ["manufacturer", "model", "sn", "location", "cost", "purchase_date", "eol_date", "notes"] #Sets the fields to use when adding an asset.

#Class based view used to update an object in the Asset model.
class AssetUpdateView(UpdateView):
    template_name="assets/updateasset.html"#Specifies the template to use when rendering the form.
    model = Asset #Specifies the model to use with this view.
    fields = ["manufacturer", "model", "sn", "location", "cost", "purchase_date", "eol_date", "notes"] #Sets the fields available to update using this view.

#View to facilitate asset deletion.
class AssetDeleteView(DeleteView):
    template_name="assets/deleteasset.html" #Specifies the template to use when rendering the page.
    model = Asset #Specifies the model this applies to.
    success_url = reverse_lazy("asset_assets") #Sets the url to redirect to as the assets list view page.
