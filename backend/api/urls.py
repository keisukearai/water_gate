# -*- coding: utf-8 -*-
from django.urls import path
import api.views as views
import api.views_gate as views_gate

# アプリケーション名
app_name = 'api'

# URL
urlpatterns = [
    # ヘッダー情報の取得
    path('header', views.HeadernfoView.as_view(), name='header'),
    # フッター情報の取得
    path('footer', views.FooterInfoView.as_view(), name='footer'),
    # エリア情報の取得
    path('area', views.AreaInfoView.as_view(), name='area'),
    # メニュー情報の取得
    path('menuinfo', views.MenuInfoView.as_view(), name='menuinfo'),
    # 水門一覧情報の取得
    path('watergatelist', views.WaterGateListView.as_view(), name='watergatelist'),
    # ゲートウェイからの受信
    path('uplink', views_gate.GwUplinkView.as_view(), name='uplink'),
    path('Uplink', views_gate.GwUplinkView.as_view(), name='Uplink'),
]