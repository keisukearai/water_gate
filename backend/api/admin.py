# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from api.models import Prefecture
from api.models import Area
from api.models import WaterGate

class PrefectureAdmin(admin.ModelAdmin):
    ordering = ("id", ) # 並び順の変更

class AreaAdmin(admin.ModelAdmin):
    ordering = ("id", ) # 並び順の変更
    def image(self, obj):
        # 大画像の存在チェック
        if obj.water_gate_map:
            return mark_safe(f'<img src="{ obj.water_gate_map.url }" style="width:5rem;">')
        return '-'

    def image_small(self, obj):
        # モバイル画像の存在チェック
        if obj.water_gate_map_sm:
            return mark_safe(f'<img src="{ obj.water_gate_map_sm.url }" style="width:3rem;margin-top:1rem;">')
        return '-'

    list_display = ('area_name', 'image', 'image_small')

class WaterGateAdmin(admin.ModelAdmin):
    ordering = ("id", ) # 並び順の変更

# 管理画面に表示
admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(WaterGate, WaterGateAdmin)