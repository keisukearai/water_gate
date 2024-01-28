# -*- coding: utf-8 -*-
import logging

from .end_device_model import EndDeviceModel

class EndDeviceLogic:
    """
    エンドデバイス ロジッククラス
    """

    def __init__(self, json_data):
        """
        コンストラクタ
        """
        # リクエストのJson形式データ
        self.json_data = json_data

    def transform(self):
        """
        モデル変換ロジック
        """
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } transform start")

        # head1部
        head1 = self.json_data['head1']
        # head2部
        head2 = self.json_data['head2']
        # data部
        data = self.json_data['data']

        # モデルインスタンス生成
        model = EndDeviceModel()
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

        logger.debug(f"{ __class__.__name__ } transform end")
        return model