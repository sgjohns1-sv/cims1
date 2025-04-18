from django.views.generic import TemplateView
from assets.models import Asset
from maintenance.models import Maintenance

# Create your views here.

class HomeView(TemplateView):
    template_name="index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["asset_count"] = Asset.objects.count()
        context["recent_maintenance"] = Maintenance.objects.filter(maint_date__year=2025)
        return context
    
