# -*- coding: utf-8 -*-
import logging
from datetime import datetime

from django.db import connection

from .model_end_device import ModelEndDevice
from .model_end_device_data import ModelEndDeviceData
from .common_logic import CommonLogic

class EndDeviceLogic:
    """
    エンドデバイス ロジッククラス
    """

    def __init__(self, json_data):
        """
        コンストラクタ

        Parameters
        ----------
        json_data: dict
            リクエスト情報
        """
        # リクエストのJson形式データ格納
        self.json_data = json_data

    def transform(self):
        """
        リクエスト→モデル変換ロジック

        Parameters
        ----------
        None

        Returns
        -------
        model: ModelEndDevice
            エンドデバイスのモデル
        """
        # ログ出力
        logger = logging.getLogger('gw_req')
        logger.debug(f"{ __class__.__name__ } transform start")

        # head1部
        head1 = self.json_data['head1']
        # head2部
        head2 = self.json_data['head2']
        # data部
        detail_data = self.json_data['data']

        # モデルインスタンス生成
        model = ModelEndDevice()
        # ゲートウェイID
        model.gw_id = head1['gwid']
        # エンドデバイスID
        model.deveui = head2['deveui']
        # 受信日時
        model.send_time = head2['time']
        # 受信 RSSI
        model.rssi = head2['rssi']
        # 受信 SNR
        model.snr = head2['snr']

        # data部変換
        data_model = self.detail_data_transform(detail_data)

        # deta部モデルに設定
        model.data_model = data_model

        logger.debug(f"{ __class__.__name__ } transform end")
        return model

    def detail_data_transform(self, detail_data):
        """
        データ部の変換ロジック

        Parameters
        ----------
        detail_data: dict
            リクエストdata部

        Returns
        -------
        model: ModelEndDeviceData
            エンドデバイスデータ部をモデル化
        """
        # ログ出力
        logger = logging.getLogger('gw_req')
        logger.debug(f"{ __class__.__name__ } detail_data_transform start")

        # 共通ロジック
        cLogic = CommonLogic()
        # 送受種別
        send_kind = detail_data[0:2]
        logger.debug(f"送信種別:{send_kind}")

        ##############################
        # モデルインスタンス生成
        ##############################
        model = ModelEndDeviceData()
        # 送信種別
        model.send_kind = send_kind

        # 装置状態
        device_status = detail_data[16:18]
        device_status_bin = cLogic.hex_to_bin(device_status)
        logger.debug(f"装置状態(2進数):{device_status_bin}")

        # 装置状態から電池残量b1を取得
        battery_level = device_status_bin[6:7]
        logger.debug(f"電池残量:{battery_level}")

        # 装置状態から通信(communication)状況b2-3を取得
        com_status_bin = device_status_bin[4:6]
        logger.debug(f"通信状況(2進数):{com_status_bin}")
        com_status = cLogic.bin_to_int(com_status_bin)
        logger.debug(f"通信状況:{com_status}")

        # ゲート状態
        # 周期送信の場合
        if model.is_period() == True:
            gate_data_status = detail_data[28:30]
        # 状変送信の場合
        else:
            gate_data_status = detail_data[30:32]
        logger.debug(f"ゲート状態(16進数変換前):{gate_data_status}")
        gate_status_bin = cLogic.hex_to_bin(gate_data_status)
        logger.debug(f"ゲート状態(2進数の8桁目):{gate_status_bin}")
        gate_status = gate_status_bin[7:]
        logger.debug(f"ゲート状態:{gate_status}")

        ##############################
        # モデルインスタンス設定
        ##############################
        # 電池残量
        model.battery_level = battery_level
        # 通信状況
        model.com_status = com_status
        # ゲート状態
        model.gate_status = gate_status

        logger.debug(f"{ __class__.__name__ } detail_data_transform end")
        return model

    def make_response_data(self, gateWay, endDevice, json_data, format_flag=True):
        """
        リクエスト返却結果を生成

        Parameters
        ----------
        gateWay: GateWay
            GateWayモデル
        endDevice: EndDevice
            EndDeviceモデル
        json_data: dict
            EndDeviceモデル
        format_flag: bool
            フォーマットフラグ

        Returns
        -------
        check: boolean
            チェック結果(True:正常、False:異常)
        ret_json: dict
            レスポンス情報
        """
        # 返却値
        check = True
        ret_json = {
            'head1': {},
            'head2': {},
            'data': "00" # 0x00 正常
        }

        # data部などのフォーマット変換エラー
        if format_flag == False:
            check = False
            ret_json['data'] = "FF" # 0xFF その他のエラー
        else:
            # DBと突合して取得できない場合
            if (gateWay == None or endDevice == None):
                check = False
                ret_json['data'] = "02" # 0x02 異常（パラメーター）

        # head1
        ret_json['head1']['kind'] = "81"
        ret_json['head1']['appeui'] = json_data['head1']['appeui']
        ret_json['head1']['gwid'] = json_data['head1']['gwid']
        ret_json['head1']['seqno'] = json_data['head1']['seqno']
        # head2
        ret_json['head2']['time'] = dt_now = datetime.now().replace(second=0, microsecond=0)
        ret_json['head2']['deveui'] = json_data['head2']['deveui']
        ret_json['head2']['devaddr'] = json_data['head2']['devaddr']
        ret_json['head2']['fport'] = json_data['head2']['fport']
        ret_json['head2']['pkttoken'] = json_data['head2']['pkttoken']
        ret_json['head2']['fmtver'] = json_data['head2']['fmtver']
        ret_json['head2']['lendt'] = "1"

        return check, ret_json
