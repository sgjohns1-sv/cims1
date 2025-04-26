from django.db import models
from django.urls import reverse
from datetime import datetime

#Model used to specify Assets in the system
class Asset(models.Model):
    #Default dates to be used for the Asset EOL and Purchase Date fields.
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
    #Method used to get the URL of a specific asset.
    def get_absolute_url(self):
        return reverse("asset_view", kwargs={"pk": self.pk})