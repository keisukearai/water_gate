# -*- coding: utf-8 -*-
import logging

from django.views.generic import TemplateView
from django.http import JsonResponse

from .models import Area
from .models import WaterGate

class AreaInfoView(TemplateView):
    """
    エリア情報の取得
    """

    def get(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # エリア情報の取得
        query = Area.objects.all()
        data = list(query.values())

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'data': data
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)

class WaterGateDetaiView(TemplateView):
    """
    水門詳細情報の取得
    """

    def get(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # リクエストパラメータの取得
        id = request.GET.get("id")

        # debug
        if int(id) >= 5:
            id = 2

        # 水門詳細情報の取得
        query = WaterGate.objects.filter(id=id)
        data = list(query.values())

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'data': data[0]
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)