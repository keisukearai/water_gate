# -*- coding: utf-8 -*-
from django.urls import path
import api.views as views

# アプリケーション名
app_name = 'api'

# URL
urlpatterns = [
    # エリア情報の取得
    path('area', views.AreaInfoView.as_view(), name='area'),
    # メニュー情報の取得
    path('menuinfo', views.MenuInfoView.as_view(), name='menuinfo'),
    # 水門一覧情報の取得
    path('watergatelist', views.WaterGateListView.as_view(), name='watergatelist'),
    # ゲートウェイからの受信
    path('uplink', views.GwUplinkView.as_view(), name='uplink'),
]