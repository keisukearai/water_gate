# -*- coding: utf-8 -*-
import logging
import json

from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import connection

from .models import GateWay
from .models import EndDevice
from .models import EndDeviceData
from .models import GateWayJsonData

from .end_device_logic import EndDeviceLogic

class GwUplinkView(TemplateView):
    """
    ゲートウェイからの受信情報の格納
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GwUplinkView, self).dispatch(*args, **kwargs)

    @csrf_exempt
    def post(self, request):
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } post start")

        # Json形式変換
        json_data = json.loads(request.body)
        logger.debug(json_data)

        # エンドデバイスロジックインスタンス生成
        elogic = EndDeviceLogic(json_data)

        try:
            # モデルへ変換
            model = elogic.transform()
        except Exception as e:
            logger.debug(e)
            # フォーマット変換エラー返却
            check, res_json = elogic.make_response_data(False, False, json_data, False)
            return JsonResponse(res_json)

        # ゲートウェイテーブルより、FKとなるidを取得
        gateWay = GateWay.objects.get_or_none(gw_id=model.gw_id)

        # エンドデバイステーブルより、FKとなるidを取得
        endDevice = EndDevice.objects.get_or_none(dev_eui=model.deveui)

        # 取得できない場合のエラー返却
        check, res_json = elogic.make_response_data(gateWay, endDevice, json_data)
        if (check == False):
            return JsonResponse(res_json)

        logger.debug(f"endDevice fk id:{endDevice.id}")
        logger.debug(f"gateWay fk id:{gateWay.id}")
        # logger.debug(type(json.dumps(json_data, indent=2)))

        # ゲートウェイJSON形式格納用パラメータ
        gateWayJsonData = GateWayJsonData(
            enddevice_id=endDevice.id,
            json_data=json_data
        )
        # 登録
        gateWayJsonData.save()

        # エンドデバイス受信格納用パラメータ
        endDeviceData = EndDeviceData(
            enddevice_id=endDevice.id,
            send_time=model.send_time,
            gate_status=model.data_model.gate_status,
            battery_level=model.data_model.battery_level,
            com_status=model.data_model.com_status,
            gate_rssi=model.rssi,
            gate_snr=model.snr
        )
        # 登録
        endDeviceData.save()

        logger.debug(f"{ __class__.__name__ } get end")
        return JsonResponse(res_json)