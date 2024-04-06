# -*- coding: utf-8 -*-

from odoo import models, fields, api


class trip_manage(models.Model):
    _name = 'trip_manage.trip_manage'
    _description = 'trip_manage.trip_manage'

    trip_name = fields.Char('申请人')
    trip_time_start = fields.Date('出差开始时间')
    trip_time_finish = fields.Date('出差结束时间')
    trip_supervisor = fields.Char('主管')
    trip_address = fields.Char('出差地点')
    trip_client = fields.Many2one('res.partner', '客户单位')
    todo_ids = fields.One2many('todo.todo', 'todo_id', '待办事宜')
    return_ids = fields.One2many('return.callback', 'return_id', '出差反馈')
    state = fields.Selection(
        [('start', '出差申请'),
         ('tenable', '出差情况反馈')], default='start', readonly=True, copy=False, track_visibility='onchange')

    return_name = fields.Char('申请人')
    return_time_start = fields.Date('出差开始时间')
    return_time_finish = fields.Date('出差结束时间')
    return_supervisor = fields.Char('主管')
    return_address = fields.Char('出差地点')
    return_client_develop = fields.Char('客户发展情况')
    return_client_unit = fields.Char('客户型号发展情况')
    return_client_manage = fields.Char('客户经营调整及变动')
    return_client_new = fields.Char('客户新型号')
    return_us_plan = fields.Char('我方开发计划及调整')
    return_client_advice = fields.Char('客户意见收集')


    def button_start(self):
        return self.write({"state": "tenable"})

    def button_tenable(self):
        return self.write({"state": "start"})


class ToDo(models.Model):
    _name = 'todo.todo'
    _description = ''

    name = fields.Char('')
    todo_id = fields.Many2one('trip_manage.trip_manage')

    todo_name = fields.Char('待办事项')
    todo_description = fields.Char('待办事项目标')


class ReturnCallback(models.Model):
    _name = 'return.callback'
    _description = ''

    name = fields.Char('')
    return_id = fields.Many2one('trip_manage.trip_manage')

    return_name = fields.Char('待办事项')
    return_description = fields.Char('待办事项目标')
    return_situation = fields.Selection(
        [('bad', '出差反馈不好'),
         ('middle', '出差反馈一般'), ('good', '出差反馈良好')], string='出差反馈情况')
    return_self_description = fields.Char('事项自我评价')
