# -*- coding: utf-8 -*-

class EndDeviceModel:
    """
    エンドデバイスモデルクラス
    """

    # ゲートウェイID
    gw_id = None
    # エンドデバイスID
    deveui = None
    # 受信日時
    send_time = None
    # 受信 RSSI
    rssi = None
    # 受信 SNR
    snr = None

    ##############################
    # getter
    ##############################
    # ゲートウェイIDのゲッター
    @property
    def gw_id(self):
        return self.__gw_id

    # エンドデバイスIDのゲッター
    @property
    def deveui(self):
        return self.__deveui

    # 受信日時のゲッター
    @property
    def send_time(self):
        return self.__send_time

    # 受信 RSSIのゲッター
    @property
    def rssi(self):
        return self.__rssi

    # 受信 SNRのゲッター
    @property
    def snr(self):
        return self.__snr

    ##############################
    # setter
    ##############################
    # ゲートウェイIDのセッター
    @gw_id.setter
    def gw_id(self, value):
        self.__gw_id = value

    # エンドデバイスIDのセッター
    @deveui.setter
    def deveui(self, value):
        self.__deveui = value

    # 受信日時のセッター
    @send_time.setter
    def send_time(self, value):
        self.__send_time = value

    # 受信 RSSIのセッター
    @rssi.setter
    def rssi(self, value):
        self.__rssi = value

    # 受信 SNRのセッター
    @snr.setter
    def snr(self, value):
        self.__snr = value