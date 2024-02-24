# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from api.models import SystemInfo
from api.models import Prefecture
from api.models import Area
from api.models import ClassInfo
from api.models import StatusInfo
from api.models import GateWay
from api.models import EndDevice
from api.models import EndDeviceData
from api.models import GateWayJsonData

class SystemInfoAdmin(admin.ModelAdmin):
    """ システム情報テーブル """
    ordering = ("id", ) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

class PrefectureAdmin(admin.ModelAdmin):
    """ 都道府県テーブル """
    ordering = ("id", ) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    list_display = ('prefecture_name',)

class AreaAdmin(admin.ModelAdmin):
    """ 地域テーブル """
    ordering = ("id", ) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def format_image(self, obj):
        # 画像の存在チェック
        if obj.water_gate_map:
            return mark_safe(f'<img src="{ obj.water_gate_map.url }" style="width:5rem;">')

    def prefecture_disp(self, obj):
        # 都道府県名
        return obj.prefecture

    # 画面表示タイトル
    prefecture_disp.short_description = Prefecture.prefecture_name.field.verbose_name

    # 画面表示タイトル
    format_image.short_description = Area.water_gate_map.field.verbose_name
    format_image.empty_value_display = "画像なし"

    list_display = ('area_name', 'prefecture_disp', 'format_image')

class ClassInfoAdmin(admin.ModelAdmin):
    """ 分類情報テーブル """
    ordering = ("id", ) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    list_display = ('class_name',)

class StatusInfoAdmin(admin.ModelAdmin):
    """ ステータス情報テーブル """
    ordering = ("id", ) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def class_code_disp(self, obj):
        # 分類名
        return obj.class_code

    # 画面表示タイトル
    class_code_disp.short_description = ClassInfo.class_name.field.verbose_name

    list_display = ('class_code_disp', 'status_code', 'status_name', 'status_supplement')

class GateWayAdmin(admin.ModelAdmin):
    """ LoRaSPN ゲートウェイテーブル """
    ordering = ("id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000
    list_display = ('gw_name', 'gw_id')

class EndDeviceAdmin(admin.ModelAdmin):
    """ LoRaWAN エンドデバイステーブル """
    ordering = ("id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def end_device_gate_no_disp(self, obj):
        # ゲート番号
        return f"({obj.end_device_gate_no})"

    # 画面表示タイトル
    end_device_gate_no_disp.short_description = EndDevice.end_device_gate_no.field.verbose_name

    list_display = ('end_device_gate_no_disp', 'end_device_name', 'dev_eui', 'gateway')

class EndDeviceDataAdmin(admin.ModelAdmin):
    """ エンドデバイス受信格納テーブル """
    ordering = ("-id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def format_send_time(self, obj):
        return obj.send_time.strftime('%Y-%m-%d %H:%M:%S')

    # 画面表示タイトル
    format_send_time.short_description = EndDeviceData.send_time.field.verbose_name
    list_display = ('enddevice', 'format_send_time')

class GateWayJsonDataAdmin(admin.ModelAdmin):
    """ ゲートウェイJSON形式格納テーブル """
    ordering = ("-id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def format_create_date(self, obj):
        return obj.create_date.strftime('%Y-%m-%d %H:%M:%S')

    # 画面表示タイトル
    format_create_date.short_description = GateWayJsonData.create_date.field.verbose_name

    list_display = ('enddevice', 'format_create_date')

# 管理画面に表示
admin.site.register(SystemInfo, SystemInfoAdmin)
admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(StatusInfo, StatusInfoAdmin)
admin.site.register(GateWay, GateWayAdmin)
admin.site.register(EndDevice, EndDeviceAdmin)
admin.site.register(EndDeviceData, EndDeviceDataAdmin)
admin.site.register(GateWayJsonData, GateWayJsonDataAdmin)