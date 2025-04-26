from django.db import models
from django.urls import reverse
from datetime import datetime
from assets.models import Asset

# Create your models here.
class Maintenance(models.Model):
    maintenance_date_default = datetime.today()

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, default=1000)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost = models.CharField(max_length=7, blank=True)
    date = models.DateTimeField(default=maintenance_date_default)
    def get_absolute_url(self):
        return reverse("maintenance_detail", kwargs={"pk": self.pk})
    
