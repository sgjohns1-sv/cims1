# Generated by Django 5.1.7 on 2025-04-15 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0025_alter_asset_asset_eoldate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_location',
            field=models.CharField(default='Science East', help_text='The room the asset is in, e.g. SE175.', max_length=50),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_eolDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 15, 6, 57, 36, 231516)),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_purchaseDate',
            field=models.DateField(default=datetime.datetime(2025, 4, 15, 6, 57, 36, 231499)),
        ),
    ]
