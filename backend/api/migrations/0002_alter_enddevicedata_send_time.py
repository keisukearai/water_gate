# Generated by Django 4.2.5 on 2024-01-21 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enddevicedata',
            name='send_time',
            field=models.DateTimeField(verbose_name='送受信日時(time)'),
        ),
    ]