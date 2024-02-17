# Generated by Django 4.2.5 on 2024-02-17 02:28

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


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
                ('water_gate_map', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format='WEBP', keep_meta=True, null=True, quality=80, scale=1, size=[1000, 800], upload_to='', verbose_name='地図画像')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '【マスタ】2.地域',
                'db_table': 'wg_area',
            },
        ),
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100, verbose_name='分類名')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '【マスタ】3.分類情報',
                'db_table': 'wg_class_info',
            },
        ),
        migrations.CreateModel(
            name='EndDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_eui', models.CharField(max_length=20, verbose_name='エンドデバイスID(deveui)')),
                ('end_device_gate_no', models.CharField(max_length=5, verbose_name='扉番号')),
                ('end_device_name', models.CharField(max_length=50, verbose_name='扉名')),
                ('end_device_gateaddress', models.CharField(blank=True, max_length=256, null=True, verbose_name='扉住所')),
                ('end_device_supplement', models.TextField(blank=True, null=True, verbose_name='補足')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '【機器】2.エンドデバイス',
                'db_table': 'wg_end_device',
            },
        ),
        migrations.CreateModel(
            name='Prefecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefecture_name', models.CharField(max_length=20, verbose_name='都道府県')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': '【マスタ】1.都道府県',
                'db_table': 'wg_prefecture',
            },
        ),
        migrations.CreateModel(
            name='StatusInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.CharField(max_length=10, verbose_name='ステータスコード')),
                ('status_name', models.CharField(max_length=100, verbose_name='ステータス名')),
                ('status_supplement', models.TextField(blank=True, null=True, verbose_name='補足')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.classinfo')),
            ],
            options={
                'verbose_name_plural': '【マスタ】4.ステータス情報',
                'db_table': 'wg_status_info',
            },
        ),
        migrations.CreateModel(
            name='GateWayJsonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_data', models.JSONField(verbose_name='JSON形式受信結果')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('enddevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.enddevice', verbose_name='エンドデバイスID')),
            ],
            options={
                'verbose_name_plural': '【機器】4.ゲートウェイJSON形式データ',
                'db_table': 'wg_gateway_json_data',
            },
        ),
        migrations.CreateModel(
            name='GateWay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gw_id', models.CharField(max_length=20, verbose_name='LoRaSPNゲートウェイID(gwid)')),
                ('gw_name', models.CharField(max_length=50, verbose_name='LoRaSPNゲートウェイ名')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area', verbose_name='地域')),
            ],
            options={
                'verbose_name_plural': '【機器】1.ゲートウェイ',
                'db_table': 'wg_gateway',
            },
        ),
        migrations.CreateModel(
            name='EndDeviceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_time', models.DateTimeField(verbose_name='送受信日時(time)')),
                ('gate_status', models.CharField(blank=True, max_length=1, null=True, verbose_name='ゲート状態(0:消灯-open, 1:全閉-close)')),
                ('battery_level', models.CharField(blank=True, max_length=1, null=True, verbose_name='電池残量(0:良, 1:低下)')),
                ('com_status', models.CharField(blank=True, max_length=1, null=True, verbose_name='通信状況(0:未受信, 1:不良, 2:普通, 3:良好)')),
                ('gate_rssi', models.IntegerField(blank=True, null=True, verbose_name='受信 RSSI')),
                ('gate_snr', models.CharField(blank=True, max_length=5, null=True, verbose_name='受信 SNR')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('enddevice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.enddevice', verbose_name='エンドデバイスID')),
            ],
            options={
                'verbose_name_plural': '【機器】3.エンドデバイス受信データ',
                'db_table': 'wg_end_device_data',
            },
        ),
        migrations.AddField(
            model_name='enddevice',
            name='gateway',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.gateway', verbose_name='ゲートウェイID'),
        ),
        migrations.AddField(
            model_name='area',
            name='prefecture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prefecture'),
        ),
    ]
