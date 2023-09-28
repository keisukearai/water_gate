# Generated by Django 4.2.5 on 2023-09-28 05:54

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_watergate_water_gate_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watergate',
            name='water_gate_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=80, scale=1, size=[500, 500], upload_to='', verbose_name='大画像'),
        ),
        migrations.AlterField(
            model_name='watergate',
            name='water_gate_image_sm',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=80, scale=1, size=[200, 200], upload_to='', verbose_name='小画像'),
        ),
    ]
