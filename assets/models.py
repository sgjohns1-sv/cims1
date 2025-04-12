from django.db import models

# Create your models here.
class Asset(models.Model):
    asset_manufacturer = models.CharField(max_length=100)
    asset_model = models.CharField(max_length=100)
    asset_sn = models.CharField(max_length=50)
    asset_cost = models.CharField(max_length=7)
    asset_purchaseDate = models.DateField
    asset_eolDate = models.DateField
    asset_owner = models.EmailField
    asset_notes = models.TextField