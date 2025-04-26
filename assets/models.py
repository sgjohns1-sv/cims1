from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Asset(models.Model):
    purchase_date_default = datetime.today()
    eol_date_default = datetime.today()
    
    manufacturer = models.CharField(max_length=100, default="")
    model = models.CharField(max_length=100, default="")
    location = models.CharField(max_length=50, default="Science East")
    sn = models.CharField(max_length=50, default="")
    cost = models.CharField(max_length=7, blank=True)
    purchase_date = models.DateField(default=purchase_date_default, blank=True)
    eol_date = models.DateField(default=eol_date_default, blank=True)
    notes = models.TextField(blank=True)
    def get_absolute_url(self):
        return reverse("asset_view", kwargs={"pk": self.pk})