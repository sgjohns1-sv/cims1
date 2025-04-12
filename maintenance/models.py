from django.db import models

# Create your models here.
class Maintenance(models.Model):
    maint_date = models.DateTimeField
    maint_description = models.TextField
    maint_title = models.CharField(max_length=100)
    maint_cost = models.CharField(max_length=7)
    maint_assetID = models.IntegerField
