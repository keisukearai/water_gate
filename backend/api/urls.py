# -*- coding: utf-8 -*-
from django.urls import path
import api.views as views

# アプリケーション名
app_name = 'api'

# URL
urlpatterns = [
    # エリア情報の取得
    path('area', views.AreaInfoView.as_view(), name='area'),
]