# -*- coding: utf-8 -*-
import logging
import json

from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Area
from .models import GateWay
from .models import EndDevice
from .models import EndDeviceData
from .models import GateWayJsonData

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
        logger.debug(f"id:{id}")

        # エリア情報の取得
        if id != '':
            query = Area.objects.filter(id=id)
        else:
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

# class WaterGateDetaiView(TemplateView):
#     """
#     水門詳細情報の取得
#     """

#     def get(self, request):
#         # ログ出力
#         logger = logging.getLogger('hp_admin')
#         logger.debug(f"{ __class__.__name__ } get start")

#         # リクエストパラメータの取得
#         id = request.GET.get("id")

#         # debug
#         if int(id) >= 5:
#             id = 2

#         # 水門詳細情報の取得
#         query = WaterGate.objects.filter(id=id)
#         data = list(query.values())

#         ##############################
#         # 出力値の設定
#         ##############################
#         params = {
#             'ret': 'ok',
#             'data': data[0]
#         }

#         logger.debug(f"{ __class__.__name__ } get end")
#         return JsonResponse(params)

class GwUplinkView(TemplateView):
    """
    ゲートウェイからの受信情報の格納
    """

    @csrf_exempt
    def post(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        # Json形式変換
        json_data = json.loads(request.body)
        logger.debug(json_data)

        # head1部
        head1 = json_data['head1']
        # head2部
        head2 = json_data['head2']
        # data部
        data = json_data['data']

        # ゲートウェイID
        gw_id = head1['gwid']
        logger.debug(f"gw_id:{gw_id}")
        # エンドデバイスID
        deveui = head2['deveui']
        logger.debug(f"deveui:{deveui}")

        # 受信日時
        send_time = head2['time']
        # ゲート状態
        # 電池残量
        # 通信状況
        # 受信 RSSI
        rssi = head2['rssi']
        # 受信 SNR
        snr = head2['snr']

        # ゲートウェイテーブルより、FKとなるidを取得
        gateWay = GateWay.objects.get(gw_id=gw_id)
        logger.debug(f"gateWay id:{gateWay.id}")

        # エンドデバイステーブルより、FKとなるidを取得
        endDevice = EndDevice.objects.get(dev_eui=deveui)
        logger.debug(f"endDevice id:{endDevice.id}")

        # TOD:取得できない場合のエラー返却

        # ゲートウェイJSON形式格納用パラメータ
        gateWayJsonData = GateWayJsonData(
            gateway_id=gateWay.id,
            json_data=json_data
        )
        # 登録
        gateWayJsonData.save()

        # エンドデバイス受信格納用パラメータ
        endDeviceData = EndDeviceData(
            enddevice_id=endDevice.id,
            send_time=send_time,
            gate_status=None,
            gate_battery_level=None,
            gate_communication=None,
            gate_rssi=rssi,
            gate_snr=snr
        )
        # 登録
        endDeviceData.save()

        ##############################
        # 出力値の設定
        ##############################
        params = {
            'ret': 'ok',
        }

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(params)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GwUplinkView, self).dispatch(*args, **kwargs)