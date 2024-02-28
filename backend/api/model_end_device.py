# -*- coding: utf-8 -*-

class ModelEndDevice:
    """
    エンドデバイスモデルクラス
    """

    # ゲートウェイID
    gw_id = None
    # エンドデバイスID
    deveui = None
    # 送受種別
    send_kind = None
    # 受信日時
    send_time = None
    # 受信 RSSI
    rssi = None
    # 受信 SNR
    snr = None
    # data部モデル
    data_model = None

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

    # 送受種別のゲッター
    @property
    def send_kind(self):
        return self.__send_kind

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

    # data部モデルのゲッター
    @property
    def data_model(self):
        return self.__data_model

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

    # 送受種別のセッター
    @send_kind.setter
    def send_kind(self, value):
        self.__send_kind = value

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

    # data部モデルのセッター
    @data_model.setter
    def data_model(self, value):
        self.__data_model = value

    ##############################
    # その他
    ##############################
    def is_period(self):
        """
        周期送信判定
        """
        if self.send_kind == '05':
            return True
        return False

    def is_state(self):
        """
        状変(状態変化)送信判定
        """
        if self.send_kind == '08':
            return True
        return False

    def get_send_kind_name(self):
        """
        送受種別名の取得
        """
        if self.send_kind == '05':
            return "周期"
        elif self.send_kind == '08':
            return "状変"
        return None