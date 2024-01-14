# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from api.models import Prefecture
from api.models import Area
from api.models import GateWay
from api.models import EndDevice
from api.models import EndDeviceData
from api.models import GateWayJsonData

class PrefectureAdmin(admin.ModelAdmin):
    """ 都道府県テーブル """
    ordering = ("id", ) # 並び順の変更
    list_display = ('prefecture_name',)

class AreaAdmin(admin.ModelAdmin):
    """ 地域テーブル """
    ordering = ("id", ) # 並び順の変更
    def image(self, obj):
        # 画像の存在チェック
        if obj.water_gate_map:
            return mark_safe(f'<img src="{ obj.water_gate_map.url }" style="width:5rem;">')
        return '-'

    list_display = ('area_name', 'image')

class GateWayAdmin(admin.ModelAdmin):
    """ LoRaSPN ゲートウェイテーブル """
    ordering = ("id",) # 並び順の変更
    list_display = ('gw_name', 'gw_id')

class EndDeviceAdmin(admin.ModelAdmin):
    """ LoRaWAN エンドデバイステーブル """
    ordering = ("id",) # 並び順の変更
    list_display = ('end_device_gate_no', 'end_device_name', 'dev_eui', 'gw_id')

class EndDeviceDataAdmin(admin.ModelAdmin):
    """ エンドデバイス受信格納テーブル """
    ordering = ("-id",) # 並び順の変更
    list_display = ('dev_eui', 'send_time')

class GateWayJsonDataAdmin(admin.ModelAdmin):
    """ ゲートウェイJSON形式格納テーブル """
    ordering = ("-id",) # 並び順の変更
    list_display = ('gw_id', 'create_date')

# 管理画面に表示
admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(GateWay, GateWayAdmin)
admin.site.register(EndDevice, EndDeviceAdmin)
admin.site.register(EndDeviceData, EndDeviceDataAdmin)
admin.site.register(GateWayJsonData, GateWayJsonDataAdmin)