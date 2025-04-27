from django.urls import reverse_lazy
from .models import Maintenance
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

#Class based view to list the maintenance records stored in the system.
class MaintenanceListView(ListView):
    template_name="maintenance/index.html"
    model = Maintenance
    def get_queryset(self):
        if ('search' not in self.request.GET.keys()):
            maintenance_list = Maintenance.objects.all()
        else:
            maintenance_list = Maintenance.objects.filter(Q(title__icontains=self.request.GET['search']) | Q(cost__icontains=self.request.GET['search']) | Q(description__icontains=self.request.GET['search']) | Q(date__icontains=self.request.GET['search']))
        return maintenance_list

#Class based view used to serve the detailed view of an asset.
class MaintenanceDetailView(DetailView):
    template_name="maintenance/detailview.html" #Specifies the template for the view to use.
    model = Maintenance #Sets the model to use for the detailed view.

#Class based view used to add maintenance records into the system.
class MaintenanceAddView(CreateView):
    template_name="maintenance/addview.html" #Specifies the template for the view to use.
    model = Maintenance #Specifies the model used for the view.
    fields = ["asset", "title", "description", "cost", "date"] #Specifies the fields available to fill out in the view.

#Class based view used to update maintenance records.
class MaintenanceUpdateView(UpdateView):
    template_name="maintenance/updateview.html" #Specifies the template for the view to use.
    model=Maintenance #Specifies the model for the view to use.
    fields = ["asset", "title", "description", "cost", "date"] #Specifies what fields the view can be used to update.

#Class based view used to delete maintenance records.
class MaintenanceDeleteView(DeleteView):
    template_name="maintenance/deleteview.html" #Specifies the template for the view to use.
    model=Maintenance #Specifies the model for the view to use.
    success_url = reverse_lazy("maintenance_list") #Sets the success or return url to be the general listing of maintenance records.