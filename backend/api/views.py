# -*- coding: utf-8 -*-
# import logging

from django.views.generic import TemplateView
from django.http import JsonResponse

from .models import Area

# Create your views here.
class AreaInfoView(TemplateView):
    """
    エリア情報の取得
    """

    def get(self, request):
        # ログ出力
        # logger = logging.getLogger('hp_admin')
        # logger.debug(f"{ __class__.__name__ } get start")

        # 会社情報の取得
        query = Area.objects.all()
        data = list(query.values())

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'data': data
        }

        # logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)