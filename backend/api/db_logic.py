# -*- coding: utf-8 -*-
import logging

from django.db import connection

class DbLogic:
    """
    DBロジッククラス
    """

    def get_device_count(self, status=None):
        """
        デバイス件数取得
        """
        # ログ出力
        logger = logging.getLogger('hp_admin')
        logger.debug(f"{ __class__.__name__ } get start")

        where_param = ""
        if status != None:
            where_param = f"where gate_status = '{status}' "

        # 件数の取得
        with connection.cursor() as cursor:
            sql = (
                'select count(*) as all_cnt '
                'from wg_end_device_data da '
                'inner join wg_end_device ed on da.enddevice_id = ed.id '
                'inner join wg_gateway gw on ed.gateway_id = gw.id '
                'where (da.enddevice_id, da.update_date) in ('
                'select enddevice_id, max(update_date) from wg_end_device_data '
                f'{where_param}'
                'group by enddevice_id '
                ')'
            )
            # logger.debug(f"sql:{sql}")
            cursor.execute(sql)
            all_count = cursor.fetchone()

        logger.debug(f"{ __class__.__name__ } get end")
        return all_count[0]
