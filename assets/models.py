from django.db import models
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Asset(models.Model):
    purchase_date_default = datetime.today()
    eol_date_default = datetime.today()
    asset_manufacturer = models.CharField(max_length=100, help_text="The manufacturer of the asset e.g. Dell, HP.")
    asset_model = models.CharField(max_length=100, help_text="The model of the asset e.g. R740.")
    asset_sn = models.CharField(max_length=50, help_text="Enter the serial number assigned by the manufacturer.")
    asset_cost = models.CharField(max_length=7,help_text="Enter the cost of the hardware. Do not include any associated services.")
    asset_purchaseDate = models.DateField(default=purchase_date_default)
    asset_eolDate = models.DateField(default=eol_date_default)
    asset_notes = models.TextField(blank=True)
    def get_absolute_url(self):
        return "/%i" % int(self.pk)