from django.db import models
from django.urls import reverse
from datetime import datetime
from assets.models import Asset

#Details the main maintenance record model.
class Maintenance(models.Model):
    maintenance_date_default = datetime.today() #Used for the default maintenance date.

    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, default=1000)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost = models.CharField(max_length=7, blank=True)
    date = models.DateTimeField(default=maintenance_date_default)
    def get_absolute_url(self):#Function used to return the exact url of objects, in this case a maintenance record.
        return reverse("maintenance_detail", kwargs={"pk": self.pk})
    
