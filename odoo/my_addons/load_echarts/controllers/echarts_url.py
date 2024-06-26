#!/usr/bin/env python
# coding=utf-8

from odoo import http
from odoo.http import request
import time
import datetime
import json
from odoo import api
from odoo.tools import misc

import logging
_logger = logging.getLogger(__name__)

#
class Academy(http.Controller):
    # 创建接口测试

    @http.route('/method/echarts/api', auth='public', type='http', methods=['POST', 'GET'], csrf=False)
    def method_echarts_api(self):
        _logger.info('调用echarts成功！')
        order_count_list = []
        complaint_orders_obj = http.request.env['linxun.complaint_case']
        # 获取本月一号
        first_day_this_month_tmp = datetime.date.today().replace(day=1)
        first_day_this_month = datetime.datetime.strftime(first_day_this_month_tmp, '%Y-%m-%d')
        for r in range(1, 10):
            o_count = complaint_orders_obj.sudo().search_count([('complaint_reason','=', r),('created_at','>=',first_day_this_month)])
            order_count_list.append(o_count)
        data_list = order_count_list
        return json.dumps([])

class Student(http.Controller):
        @http.route('/student/student', auth='user', website=True)
        def list(self, **kwargs):
            obj = http.request.env['student.student']
            objs = obj.search([])
            print(http.request.website.id)
            return http.request.render(
                'student.student_student_template', {'objs': objs}
            )

        @http.route('/get_school/type1', type='http', auth='none', website=True)
        def get_school_http(self):
            print(http.request.website.id)

            people_data = [
                {

                    'value': record.value,
                    'name': record.name,

                }
                for record in request.env['school.school'].sudo().search([])
            ]


            return json.dumps(people_data)

