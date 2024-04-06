# -*- coding: utf-8 -*-

from odoo import models, fields, api


class client_hospitality(models.Model):
    _name = 'client_hospitality.client_hospitality'
    _description = 'client_hospitality.client_hospitality'
    _inherit = ['mail.thread']

    client_name = fields.Many2one('res.partner', string='来客单位')
    client_visit_time = fields.Date('来客时间')
    client_member_ids = fields.One2many('client.member','client_member_id','来客人员')
    car_member_ids = fields.One2many('client.car', 'car_member_id', '接待用车安排')
    work_member_ids = fields.One2many('client.work','work_member_id','来客到公司工作计划安排')
    relate_member_ids = fields.One2many('client.relate','relate_member_id','责任人信息')


class ClientMember(models.Model):
    _name = 'client.member'
    _description = ''

    name = fields.Char('')
    client_member_id = fields.Many2one('client_hospitality.client_hospitality', '')

    client_member_name = fields.Char('姓名')
    client_member_unit = fields.Many2one('res.partner','单位')
    client_member_duty = fields.Char('职务')
    client_member_hotel = fields.Char('住房安排')
    client_member_phone = fields.Char('联系电话')

class ClientCar(models.Model):
    _name = 'client.car'
    _description = ''

    name = fields.Char('')
    car_member_id = fields.Many2one('client_hospitality.client_hospitality', '')

    car_member_time = fields.Date('用车时间')
    car_member_togo = fields.Char('去向')
    car_member_number = fields.Char('人数')
    car_member_duty = fields.Char('安排')

class ClientWork(models.Model):
    _name = 'client.work'
    _description = ''

    name = fields.Char('')
    work_member_id = fields.Many2one('client_hospitality.client_hospitality', '')

    work_member_time = fields.Date('时间')
    car_member_togo = fields.Char('工作内容')

class ClientRelate(models.Model):
    _name = 'client.relate'
    _description = ''

    name = fields.Char('')
    relate_member_id = fields.Many2one('client_hospitality.client_hospitality', '')

    relate_code = fields.Char('序号')
    relate_department = fields.Char('责任部门')
    relate_person = fields.Char('客户联系人')
    relate_duty = fields.Char('职务')
    relate_telephone = fields.Char('联系方式')









