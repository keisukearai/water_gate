# -*- coding: utf-8 -*-
from django.db import models

class Prefecture(models.Model):
    """
    都道府県テーブル
    """
    prefecture_name = models.CharField(verbose_name="都道府県", max_length=20)

    class Meta:
        db_table = 'prefecture'
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

    class Meta:
        db_table = 'area'
        verbose_name = f"{ db_table } (地域)"
        verbose_name_plural = f"{ db_table } (地域)"

    def __str__(self):
        return self.area_name

class WaterGate(models.Model):
    """
    水門テーブル
    """
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    water_gate_name = models.CharField(verbose_name="水門名", max_length=50)
    water_gateaddress = models.CharField(verbose_name="住所", max_length=256)
    water_gate_supplement = models.TextField(verbose_name="補足", blank=True, null=True)
    latitude = models.DecimalField(verbose_name="緯度", max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(verbose_name="経度", max_digits=9, decimal_places=6, default=0)

    class Meta:
        db_table = 'watergate'
        verbose_name = f"{ db_table } (水門)"
        verbose_name_plural = f"{ db_table } (水門)"

    def __str__(self):
        return self.water_gate_name