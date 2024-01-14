# -*- coding: utf-8 -*-
from django.db import models
from django_resized import ResizedImageField

class Prefecture(models.Model):
    """
    都道府県テーブル
    """
    prefecture_name = models.CharField(verbose_name="都道府県", max_length=20)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_prefecture'
        verbose_name_plural = "【マスタ】1.都道府県"

    def __str__(self):
        return self.prefecture_name

class Area(models.Model):
    """
    地域テーブル
    """
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    area_name = models.CharField(verbose_name="地域名", max_length=100)
    area_supplement = models.TextField(verbose_name="補足", blank=True, null=True)
    water_gate_map = ResizedImageField(verbose_name="地図画像", size=[1000, 800], crop=['middle', 'center'], force_format="WEBP", upload_to='', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_area'
        verbose_name_plural = "【マスタ】2.地域"

    def __str__(self):
        return self.area_name

class GateWay(models.Model):
    """
    LoRaSPN ゲートウェイテーブル
    """
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="地域")
    gw_id = models.CharField(verbose_name="LoRaSPNゲートウェイID", max_length=20)
    gw_name = models.CharField(verbose_name="LoRaSPNゲートウェイ名", max_length=50)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_gateway'
        verbose_name_plural = "【機器】1.LoRaSPNゲートウェイ"

    def __str__(self):
        return f"【{self.gw_name}】{self.gw_id}"

class EndDevice(models.Model):
    """
    LoRaWAN エンドデバイステーブル
    """
    gw_id = models.ForeignKey(GateWay, on_delete=models.CASCADE, verbose_name="ゲートウェイID")
    dev_eui = models.CharField(verbose_name="エンドデバイスID", max_length=20)
    end_device_gate_no = models.CharField(verbose_name="扉番号", max_length=5)
    end_device_name = models.CharField(verbose_name="扉名", max_length=50)
    end_device_gateaddress = models.CharField(verbose_name="扉住所", max_length=256, blank=True, null=True)
    end_device_supplement = models.TextField(verbose_name="補足", blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_end_device'
        verbose_name_plural = "【機器】2.LoRaWANエンドデバイス"

    def __str__(self):
        return f"【{self.end_device_gate_no}】{self.end_device_name} - {self.dev_eui}"

class EndDeviceData(models.Model):
    """
    エンドデバイス受信格納テーブル
    """
    dev_eui = models.ForeignKey(EndDevice, on_delete=models.CASCADE, verbose_name="エンドデバイスID")
    send_time = models.DateTimeField(verbose_name="受信日時")
    gate_status = models.CharField(verbose_name="ゲート状態", max_length=1, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_end_device_data'
        verbose_name_plural = "【機器】3.LoRaWANエンドデバイス受信データ"

    # def __str__(self):
    #     return self.dev_eui

class GateWayJsonData(models.Model):
    """
    ゲートウェイJSON形式格納テーブル
    """
    gw_id = models.ForeignKey(GateWay, on_delete=models.CASCADE, verbose_name="ゲートウェイ")
    json_data = models.JSONField(verbose_name="JSON形式受信結果")
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)

    class Meta:
        db_table = 'wg_gateway_json_data'
        verbose_name_plural = "【機器】4.ゲートウェイJSON形式データ"

    # def __str__(self):
    #     return self.gw_id