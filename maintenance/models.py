from django.db import models
from django.urls import reverse
from datetime import datetime
from assets.models import Asset

# Create your models here.
class Maintenance(models.Model):
    maintenance_date_default = datetime.today()

    maint_assetID = models.ForeignKey(Asset, on_delete=models.CASCADE, default=1000)
    maint_title = models.CharField(max_length=100)
    maint_description = models.TextField(blank=True)
    maint_cost = models.CharField(max_length=7)
    maint_date = models.DateTimeField(default=maintenance_date_default)
    def get_absolute_url(self):
        return reverse("", kwargs={"pk": self.pk})
    
