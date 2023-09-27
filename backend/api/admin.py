# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from api.models import Prefecture
from api.models import Area
from api.models import WaterGate

class PrefectureAdmin(admin.ModelAdmin):
    ordering = ("id", ) # 並び順の変更

class AreaAdmin(admin.ModelAdmin):
    ordering = ("id", ) # 並び順の変更

# 管理画面に表示
admin.site.register(Prefecture, PrefectureAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(WaterGate)