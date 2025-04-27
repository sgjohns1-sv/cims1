from django.views.generic import TemplateView
from assets.models import Asset
from maintenance.models import Maintenance
from datetime import datetime,timedelta


#Class based template view

class HomeView(TemplateView):
    template_name="home/index.html" #Sets the name of the template to be used to render the page.
    def get_context_data(self, **kwargs): #Function to return the context to be used when rendering the home page.
        context = super().get_context_data(**kwargs)
        context["asset_count"] = Asset.objects.count() #Gets the current count of assets in the system.
        context["recent_maintenance"] = Maintenance.objects.filter(date__gt=datetime.today() - timedelta(days=7)) #Gets the most recent maintenance records from the last 7 days.
        return context
    
