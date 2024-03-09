# -*- coding: utf-8 -*-

class ModelEndDeviceData:
    """
    エンドデバイスデータ部モデルクラス
    """

    # 送信種別(周期)
    SEND_KIND_PERIOD = '05'
    # 送信種別(状変)
    SEND_KIND_STATE = '07'
    # 送信種別(テスト)
    SEND_KIND_TEST = '15'

    # 送受種別
    send_kind = None
    # 電池残量
    battery_level = None
    # 通信(communication)状況
    com_status = None
    # ゲート状態
    gate_status = None

    ##############################
    # getter
    ##############################
    # 送受種別のゲッター
    @property
    def send_kind(self):
        return self.__send_kind

    # 電池残量のゲッター
    @property
    def battery_level(self):
        return self.__battery_level

    # 通信状況のゲッター
    @property
    def com_status(self):
        return self.__com_status

    # ゲート状態のゲッター
    @property
    def gate_status(self):
        return self.__gate_status

    ##############################
    # setter
    ##############################
    # 送受種別のセッター
    @send_kind.setter
    def send_kind(self, value):
        self.__send_kind = value

    # 電池残量のセッター
    @battery_level.setter
    def battery_level(self, value):
        self.__battery_level = value

    # 通信状況のセッター
    @com_status.setter
    def com_status(self, value):
        self.__com_status = value

    # ゲート状態のセッター
    @gate_status.setter
    def gate_status(self, value):
        self.__gate_status = value

##############################
    # その他
    ##############################
    def is_period(self):
        """
        周期送信判定
        """
        if self.send_kind in (self.SEND_KIND_PERIOD, self.SEND_KIND_TEST):
            return True
        return False

    def is_state(self):
        """
        状変(状態変化)送信判定
        """
        if self.send_kind == self.SEND_KIND_STATE:
            return True
        return False

    def get_send_kind_name(self):
        """
        送受種別名の取得
        """
        if self.send_kind == self.SEND_KIND_PERIOD:
            return "周期"
        elif self.send_kind == self.SEND_KIND_STATE:
            return "状変"
        elif self.send_kind == self.SEND_KIND_TEST:
            return "テスト"
        return None