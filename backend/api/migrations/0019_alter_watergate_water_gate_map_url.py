# Generated by Django 4.2.5 on 2023-10-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_watergate_water_gate_map_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watergate',
            name='water_gate_map_url',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='GoogleMapのIframeのsrc'),
        ),
    ]