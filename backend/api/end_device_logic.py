# -*- coding: utf-8 -*-
import logging

from .model_end_device import ModelEndDevice
from .model_end_device_data import ModelEndDeviceData

class EndDeviceLogic:
    """
    エンドデバイス ロジッククラス
    """

    def __init__(self, json_data):
        """
        コンストラクタ
        """
        # リクエストのJson形式データ格納
        self.json_data = json_data

    def transform(self):
        """
        リクエスト→モデル変換ロジック
        """
        # ログ出力
        logger = logging.getLogger('hp_admin')
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
        # detaモデルに設定
        model.data_model = data_model

        logger.debug(f"{ __class__.__name__ } transform end")
        return model

    def detail_data_transform(self, detail_data):
        """
        データ部の変換ロジック
        """
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } detail_data_transform start")

        # 装置状態
        device_status = detail_data[16:18]
        device_status_bin = self.hex_to_bin(device_status)
        logger.debug(f"装置状態(2進数):{device_status_bin}")

        # 装置状態から電池残量b1を取得
        battery_level = device_status_bin[6:7]
        logger.debug(f"電池残量:{battery_level}")

        # 装置状態から通信(communication)状況b2-3を取得
        com_status_bin = device_status_bin[4:6]
        logger.debug(f"通信状況(2進数):{com_status_bin}")
        com_status = self.bin_to_int(com_status_bin)
        logger.debug(f"通信状況:{com_status}")

        # ゲート状態
        gate_data_status = detail_data[28:30]
        gate_status_bin = self.hex_to_bin(gate_data_status)
        logger.debug(f"ゲート状態(2進数):{gate_status_bin}")
        gate_status = gate_status_bin[7:]
        logger.debug(f"ゲート状態:{gate_status}")

        # モデルインスタンス生成
        model = ModelEndDeviceData()
        # 電池残量
        model.battery_level = battery_level
        # 通信状況
        model.com_status = com_status
        # ゲート状態
        model.gate_status = gate_status

        logger.debug(f"{ __class__.__name__ } detail_data_transform end")
        return model

    def hex_to_bin(self, hs):
        """
        16進数から2進数への変換(パラメータに0xを付与して16進数として処理する)

        Parameters
        ----------
        hs : str
            16進数のバイト部分

        Returns
        -------
        n_bin : str
            8桁の2進数形式の文字列
        """
        # 16進数の形の文字列へ変換
        hex_s = f"0x{hs}"
        # 数値へ
        hex_i = int(hex_s, 16)
        # 8桁の2進数に変換
        n_bin = format(hex_i, "08b")
        return n_bin

    def bin_to_int(self, bi):
        """
        2進数から10進数への変換

        Parameters
        ----------
        bi : str
            2進数のバイト部分

        Returns
        -------
        n_int : str
            10進数形式の文字列
        """
        return str(int(bi, 2))
