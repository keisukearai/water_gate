# Generated by Django 4.2.5 on 2023-09-27 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100, verbose_name='地域名')),
                ('area_supplement', models.TextField(blank=True, null=True, verbose_name='補足')),
            ],
            options={
                'verbose_name': 'area (地域)',
                'verbose_name_plural': 'area (地域)',
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefecture_name', models.CharField(max_length=20, verbose_name='都道府県')),
            ],
            options={
                'verbose_name': 'prefecture (都道府県)',
                'verbose_name_plural': 'prefecture (都道府県)',
                'db_table': 'prefecture',
            },
        ),
        migrations.CreateModel(
            name='WaterGate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_gate_name', models.CharField(max_length=50, verbose_name='水門名')),
                ('water_gateaddress', models.CharField(max_length=256, verbose_name='住所')),
                ('water_gate_supplement', models.TextField(blank=True, null=True, verbose_name='補足')),
                ('water_gate_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像')),
                ('water_gate_latitude', models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='緯度')),
                ('water_gate_longitude', models.DecimalField(decimal_places=6, default=0, max_digits=9, verbose_name='経度')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area', verbose_name='地域')),
            ],
            options={
                'verbose_name': 'watergate (水門)',
                'verbose_name_plural': 'watergate (水門)',
                'db_table': 'watergate',
            },
        ),
        migrations.AddField(
            model_name='area',
            name='prefecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prefecture'),
        ),
    ]
