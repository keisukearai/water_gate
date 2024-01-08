# -*- coding: utf-8 -*-
from django.db import models
from django_resized import ResizedImageField

class Prefecture(models.Model):
    """
    都道府県テーブル
    """
    prefecture_name = models.CharField(verbose_name="都道府県", max_length=20)

    class Meta:
        db_table = 'wg_prefecture'
        verbose_name = f"{ db_table } (都道府県)"
        verbose_name_plural = f"{ db_table } (都道府県)"

    def __str__(self):
        return self.prefecture_name

class Area(models.Model):
    """
    地域テーブル
    """
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    area_name = models.CharField(verbose_name="地域名", max_length=100)
    area_supplement = models.TextField(verbose_name="補足", blank=True, null=True)
    water_gate_map = ResizedImageField(verbose_name="地図大画像", size=[1000, 800], crop=['middle', 'center'], force_format="WEBP", upload_to='', blank=True, null=True)
    water_gate_map_sm = ResizedImageField(verbose_name="地図小画像", size=[400, 320], crop=['middle', 'center'], force_format="WEBP", upload_to='', blank=True, null=True)

    class Meta:
        db_table = 'wg_area'
        verbose_name = f"{ db_table } (地域)"
        verbose_name_plural = f"{ db_table } (地域)"

    def __str__(self):
        return self.area_name

class WaterGate(models.Model):
    """
    水門・陸閘基本テーブル
    """
    area = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="地域")
    water_gate_no = models.CharField(verbose_name="扉番号", max_length=10)
    water_gate_name = models.CharField(verbose_name="扉名", max_length=50)
    water_gateaddress = models.CharField(verbose_name="扉住所", max_length=256)
    water_gate_supplement = models.TextField(verbose_name="補足", blank=True, null=True)

    class Meta:
        db_table = 'wg_base'
        verbose_name = f"{ db_table } (水門・陸閘)"
        verbose_name_plural = f"{ db_table } (水門・陸閘)"

    def __str__(self):
        return f"【{self.water_gate_no}】{self.water_gate_name}"