# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

from .common_logic import CommonLogic

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

    # 画面一覧表示項目
    list_display = ('prefecture_name',)

class AreaAdmin(admin.ModelAdmin):
    """ 地域テーブル """

    ordering = ("id", ) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def disp_prefecture(self, obj):
        # 都道府県名
        return obj.prefecture

    # 都道府県のタイトル
    disp_prefecture.short_description = Prefecture.prefecture_name.field.verbose_name

    def format_image(self, obj):
        # 画像の存在チェック
        if obj.water_gate_map:
            return mark_safe(f'<img src="{ obj.water_gate_map.url }" style="width:5rem;">')

    # 画像のタイトル
    format_image.short_description = Area.water_gate_map.field.verbose_name
    # 画像なしの場合
    format_image.empty_value_display = "画像なし"

    # 画面一覧表示項目
    list_display = ('area_name', 'disp_prefecture', 'format_image')

class ClassInfoAdmin(admin.ModelAdmin):
    """ 分類情報テーブル """

    ordering = ("id", ) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    # 画面一覧表示項目
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

    # 画面一覧表示項目
    list_display = ('class_code_disp', 'status_code', 'status_name', 'status_supplement')

class GateWayAdmin(admin.ModelAdmin):
    """ LoRaSPN ゲートウェイテーブル """

    ordering = ("id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def disp_gw_name(self, obj):
        return f"【{obj.gw_name}】{obj.gw_id}"

    # 画面表示のタイトル
    disp_gw_name.short_description = "ゲートウェイID"

    def disp_is_disp(self, obj):
        # 画面表示有無
        if obj.is_disp == True:
            return "あり"
        return ""

    # 画面表示のタイトル
    disp_is_disp.short_description = GateWay.is_disp.field.verbose_name

    # 画面一覧表示項目
    list_display = ('disp_gw_name', 'disp_is_disp', 'create_date', 'update_date')

class EndDeviceAdmin(admin.ModelAdmin):
    """ LoRaWAN エンドデバイステーブル """

    ordering = ("id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def disp_end_device_gate_no(self, obj):
        # エンドデバイス
        return f"扉番号({obj.end_device_gate_no}){obj.end_device_name} - {obj.dev_eui}"

    # エンドデバイスのタイトル
    disp_end_device_gate_no.short_description = "エンドデバイス"

    def disp_is_disp(self, obj):
        # 画面表示有無
        if obj.is_disp == True:
            return "あり"
        return ""

    # 画面表示のタイトル
    disp_is_disp.short_description = EndDevice.is_disp.field.verbose_name

    # 画面一覧表示項目
    list_display = ('disp_end_device_gate_no', 'disp_is_disp', 'gateway', 'create_date', 'update_date')

class EndDeviceDataAdmin(admin.ModelAdmin):
    """ エンドデバイス受信格納テーブル """

    ordering = ("-id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def disp_enddevice(self, obj):
        return f"扉番号{obj.enddevice}"

    # 画面表示タイトル
    disp_enddevice.short_description = "エンドデバイス"

    # ゲート状態
    def disp_gate_status(self, obj):
        data = StatusInfo.objects.filter(class_code='1', status_code=obj.gate_status).first()
        if data == None:
            return ''
        return f"{obj.gate_status}:{data.status_name}"

    # ゲート状態のタイトル
    disp_gate_status.short_description = EndDeviceData.gate_status.field.verbose_name

    # 電池状態
    def disp_battery_level(self, obj):
        data = StatusInfo.objects.filter(class_code='2', status_code=obj.battery_level).first()
        if data == None:
            return ''
        return f"{obj.battery_level}:{data.status_name}"

    # 電池状態のタイトル
    disp_battery_level.short_description = EndDeviceData.battery_level.field.verbose_name

    # 通信状況
    def disp_com_status(self, obj):
        data = StatusInfo.objects.filter(class_code='3', status_code=obj.com_status).first()
        if data == None:
            return ''
        return f"{obj.com_status}:{data.status_name}"

    # 通信状況のタイトル
    disp_com_status.short_description = EndDeviceData.com_status.field.verbose_name

    # 送受信日時フォーマット
    def disp_send_time(self, obj):
        "時刻jst変換"
        return CommonLogic().utc_to_jst(obj.send_time)

    # 送受信日時のタイトル
    disp_send_time.short_description = EndDeviceData.send_time.field.verbose_name

    # 画面一覧表示項目
    list_display = ('disp_enddevice', 'id', 'send_kind', 'disp_gate_status', 'disp_battery_level', 'disp_com_status', 'disp_send_time')

    # 検索窓(扉番号、扉名、エンドデバイスID)
    search_fields = ['enddevice__end_device_gate_no', 'enddevice__end_device_name', 'enddevice__dev_eui']

class GateWayJsonDataAdmin(admin.ModelAdmin):
    """ ゲートウェイJSON形式格納テーブル """

    ordering = ("-id",) # 並び順の変更
    # 1ページ当たりに表示する件数
    list_per_page = 20
    # 全件表示を許容する最大件数
    list_max_show_all = 5000

    def disp_enddevice(self, obj):
        "エンドデバイス"
        return f"扉番号{obj.enddevice}"

    # エンドデバイスのタイトル
    disp_enddevice.short_description = "エンドデバイス"

    def disp_create_date(self, obj):
        "時刻jst変換"
        return CommonLogic().utc_to_jst(obj.create_date)

    # 画面表示タイトル
    disp_create_date.short_description = GateWayJsonData.create_date.field.verbose_name

    # 画面一覧表示項目
    list_display = ('disp_enddevice', 'id', 'disp_create_date')

    # 検索窓(扉番号、扉名、エンドデバイスID)
    search_fields = ['enddevice__end_device_gate_no', 'enddevice__end_device_name', 'enddevice__dev_eui']

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