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

        # data部変換
        self.detail_data_transform(detail_data)

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

        logger.debug(f"{ __class__.__name__ } detail_data_transform end")
        return

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
