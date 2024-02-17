# -*- coding: utf-8 -*-
import logging

from django.db import connection

class DbLogic:
    """
    DBロジッククラス
    """

    def get_device_count(self):
        """
        デバイス件数取得
        """
        # 件数の取得
        with connection.cursor() as cursor:
            sql = (
                'select count(*) as all_cnt '
                'from wg_end_device_data da '
                'inner join wg_end_device ed on da.enddevice_id = ed.id '
                'inner join wg_gateway gw on ed.gateway_id = gw.id '
                'where (da.enddevice_id, da.update_date) in ('
                'select enddevice_id, max(update_date) from wg_end_device_data group by enddevice_id'
                ')'
            )
            cursor.execute(sql)
            all_count = cursor.fetchone()

        return all_count[0]