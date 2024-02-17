# -*- coding: utf-8 -*-

class ModelEndDeviceData:
    """
    エンドデバイスデータ部モデルクラス
    """

    # 電池残量
    battery_level = None
    # 通信(communication)状況
    com_status = None
    # ゲート状態
    gate_status = None

    ##############################
    # getter
    ##############################
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
