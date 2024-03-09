# -*- coding: utf-8 -*-
from django.db import models
from django_resized import ResizedImageField

class BaseManager(models.Manager):
   def get_or_none(self, **kwargs):
       """
       検索にヒットすればそのモデルを、しなければNoneを返します。
       """
       try:
           return self.get_queryset().get(**kwargs)
       except self.model.DoesNotExist:
           return None

class SystemInfo(models.Model):
    """
    システム情報テーブル
    """
    objects = BaseManager()
    system_name = models.CharField(verbose_name="名称", max_length=100)
    system_value = models.CharField(verbose_name="値", max_length=1024, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_system_info'
        verbose_name_plural = "【マスタ】1.システム情報"

    def __str__(self):
        return f"【{self.system_name}】{self.system_value}"

class Prefecture(models.Model):
    """
    都道府県テーブル
    """
    prefecture_name = models.CharField(verbose_name="都道府県", max_length=20)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_prefecture'
        verbose_name_plural = "【マスタ】2.都道府県"

    def __str__(self):
        return self.prefecture_name

class Area(models.Model):
    """
    地域テーブル
    """
    objects = BaseManager()
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    area_name = models.CharField(verbose_name="地域名", max_length=100)
    area_supplement = models.TextField(verbose_name="補足", blank=True, null=True)
    water_gate_map = ResizedImageField(verbose_name="地図画像", size=[1000, 800], crop=['middle', 'center'], force_format="WEBP", upload_to='', blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_area'
        verbose_name_plural = "【マスタ】3.地域"

    def __str__(self):
        return self.area_name

class ClassInfo(models.Model):
    """
    分類情報テーブル
    """
    class_name = models.CharField(verbose_name="分類名", max_length=100)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_class_info'
        verbose_name_plural = "【マスタ】4.分類情報"

    def __str__(self):
        return self.class_name

class StatusInfo(models.Model):
    """
    ステータス情報テーブル
    """
    class_code = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
    status_code = models.CharField(verbose_name="ステータスコード", max_length=10)
    status_name = models.CharField(verbose_name="ステータス名", max_length=100)
    status_supplement = models.TextField(verbose_name="補足", blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_status_info'
        verbose_name_plural = "【マスタ】5.ステータス情報"

    def __str__(self):
        return self.status_name

class GateWay(models.Model):
    """
    ゲートウェイテーブル
    """
    objects = BaseManager()
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="地域")
    gw_id = models.CharField(verbose_name="LoRaSPNゲートウェイID(gwid)", max_length=20)
    gw_name = models.CharField(verbose_name="LoRaSPNゲートウェイ名", max_length=50)
    is_disp = models.BooleanField(verbose_name='画面表示', default=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_gateway'
        verbose_name_plural = "【機器】1.ゲートウェイ"

    def __str__(self):
        return f"【{self.gw_name}】{self.gw_id}"

class EndDevice(models.Model):
    """
    エンドデバイステーブル
    """
    objects = BaseManager()
    gateway = models.ForeignKey(GateWay, on_delete=models.CASCADE, verbose_name="ゲートウェイID")
    dev_eui = models.CharField(verbose_name="エンドデバイスID(deveui)", max_length=20)
    end_device_gate_no = models.CharField(verbose_name="扉番号", max_length=5)
    end_device_name = models.CharField(verbose_name="扉名", max_length=50)
    end_device_gateaddress = models.CharField(verbose_name="扉住所", max_length=256, blank=True, null=True)
    end_device_supplement = models.TextField(verbose_name="補足", blank=True, null=True)
    is_disp = models.BooleanField(verbose_name='画面表示', default=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_end_device'
        verbose_name_plural = "【機器】2.エンドデバイス"

    def __str__(self):
        return f"({self.end_device_gate_no}){self.end_device_name} - {self.dev_eui}"

class EndDeviceData(models.Model):
    """
    エンドデバイス受信格納テーブル
    """
    enddevice = models.ForeignKey(EndDevice, on_delete=models.CASCADE, verbose_name="エンドデバイスID")
    send_kind = models.CharField(verbose_name="送受種別", max_length=3, blank=True, null=True)
    send_time = models.DateTimeField(verbose_name="送受信日時(time)")
    gate_status = models.CharField(verbose_name="ゲート状態", max_length=1, blank=True, null=True)
    battery_level = models.CharField(verbose_name="電池残量", max_length=1, blank=True, null=True)
    com_status = models.CharField(verbose_name="通信状況", max_length=1, blank=True, null=True)
    gate_rssi = models.IntegerField(verbose_name="受信 RSSI", blank=True, null=True)
    gate_snr = models.CharField(verbose_name="受信 SNR", max_length=5, blank=True, null=True)
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    update_date = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    class Meta:
        db_table = 'wg_end_device_data'
        verbose_name_plural = "【機器】3.エンドデバイス受信データ"

class GateWayJsonData(models.Model):
    """
    ゲートウェイからのエンドデバイスJSON形式格納テーブル
    """
    enddevice = models.ForeignKey(EndDevice, on_delete=models.CASCADE, verbose_name="エンドデバイスID")
    json_data = models.JSONField(verbose_name="JSON形式受信結果")
    create_date = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)

    class Meta:
        db_table = 'wg_gateway_json_data'
        verbose_name_plural = "【機器】4.ゲートウェイJSON形式データ"
