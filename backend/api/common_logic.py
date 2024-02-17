# -*- coding: utf-8 -*-
import logging

class CommonLogic:
    """
    共通ロジッククラス
    """

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

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
