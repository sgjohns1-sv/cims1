# Generated by Django 5.1.7 on 2025-04-12 21:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_asset_asset_eoldate_asset_asset_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_eolDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 12, 17, 1, 12, 959527)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_purchaseDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 12, 17, 1, 12, 959503)),
        ),
    ]
