# -*- coding: utf-8 -*-
import logging
import json

from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db import connection

from .models import SystemInfo
from .models import Area

from .common_logic import CommonLogic
from .db_logic import DbLogic

class HeadernfoView(TemplateView):
    """
    ヘッダー情報の取得
    """

    def get(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # 情報取得(タイトル)
        query = SystemInfo.objects.filter(id=1)
        data = list(query.values())

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'header_title': data[0]['system_value']
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)

class FooterInfoView(TemplateView):
    """
    フッター情報の取得
    """

    def get(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # 情報取得(コピーライト)
        query = SystemInfo.objects.filter(id=2)
        cp_data = list(query.values())

        # 情報取得(URL)
        query = SystemInfo.objects.filter(id=3)
        cp_url_data = list(query.values())

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'copy_right': cp_data[0]['system_value'],
            'copy_right_url': cp_url_data[0]['system_value']
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)

class AreaInfoView(TemplateView):
    """
    エリア情報の取得
    """

    def get(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # リクエストパラメータの取得
        id = request.GET.get("id")
        # 情報取得
        query = Area.objects.filter(id=id)
        data = list(query.values())

        # 取得できない場合
        if len(data) == 0:
            data = [{"water_gate_map": "", "area_name": ""}]
        # logger.debug(data)

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'data': data
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)

class MenuInfoView(TemplateView):
    """
    メニュー情報の取得
    """

    def get(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # 共通ロジック
        dbLogic = DbLogic()

        # エリア情報の取得
        query = Area.objects.all()
        area = list(query.values())

        # 件数の取得
        all_count = dbLogic.get_device_count()
        logger.debug(f"all_count:{all_count}")

        # Openの件数
        open_count = dbLogic.get_device_count("0")
        logger.debug(f"open_count:{open_count}")

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'area': area,
            'all_count': all_count,
            'open_count': open_count,
            'close_count': all_count - open_count
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)

class WaterGateListView(TemplateView):
    """
    水門一覧情報の取得
    """

    def get(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # 共通ロジック
        cLogic = CommonLogic()
        dbLogic = DbLogic()

        # リクエストパラメータの取得
        area_id = request.GET.get("area_id")
        # 表示件数
        limit = request.GET.get("limit", 2)
        if str(limit).isdigit() == False:
            limit = 2

        # skip
        offset = request.GET.get("skip", 0)
        if str(offset).isdigit() == False:
            offset = 0

        # 状態選択
        state = request.GET.get("state", None)
        state_param = ""
        if state in ('0', '1'):
            state_param = f"and gate_status = '{state}' "
        else:
            state = None
        logger.debug(f"state:{state}")

        # エリア情報を取得
        area = Area.objects.get_or_none(id=area_id)
        area_param = ""
        if area != None:
            area_param = f"and gw.area_id = '{area.id}' "

        # 件数の取得
        all_count = dbLogic.get_device_count(state)
        logger.debug(f"all_count:{all_count}")

        # ページ情報
        pages = divmod(int(all_count), int(limit))
        if pages[1] > 0:
            totalPages = pages[0] + 1
        else:
            totalPages = pages[0]

        # 一覧情報を取得
        with connection.cursor() as cursor:
            sql = (
                'select ed.id, ed.end_device_gate_no, ed.end_device_name, '
                'da.gate_status as gate_status_code, sg.status_name as gate_status, '
                'sb.status_name as battery_level, sc.status_name as com_status, '
                'gw.gw_name '
                'from wg_end_device_data da '
                'inner join wg_end_device ed on da.enddevice_id = ed.id '
                'inner join wg_gateway gw on ed.gateway_id = gw.id '
                'left outer join wg_status_info sg on da.gate_status = sg.status_code and sg.class_code_id = 1 '
                'left outer join wg_status_info sb on da.battery_level = sb.status_code and sb.class_code_id = 2 '
                'left outer join wg_status_info sc on da.com_status = sc.status_code and sc.class_code_id = 3 '
                'where (da.enddevice_id, da.id) in ('
                'select enddevice_id, max(id) from wg_end_device_data group by enddevice_id'
                ')'
                f'{area_param} '
                f'{state_param}'
                'order by ed.end_device_gate_no '
                f'limit {limit} offset {offset}'
            )
            cursor.execute(sql)
            data = cLogic.dictfetchall(cursor)

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
            'totalPages': totalPages,
            'allCount': all_count,
            'data': data
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)
