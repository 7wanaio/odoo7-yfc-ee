# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # dob = fields.Date('Dob')

    client_code = fields.Char('信用代码', tracking=True)
    client_name = fields.Char('客户名称')
    crm_name_simple = fields.Char('客户简称')
    client_category = fields.Selection(
        [('strategic', '战略客户'), ('common', '普通客户'), ('potential_strategic', '潜在战略客户'),
         ('potential', '潜在客户'), ('importance', '重要客户')], default='common',
        string='客户类型')
    crm_type = fields.Selection([('sky', '航空2'), ('universal', '航天'), ('army', '军工厂')], string='隶属行业')
    crm_location = fields.Selection(
        [('west_south', '西南'), ('east_north', '东北'), ('east_south', '东南'), ('west_north', '西北')],
        string='隶属片区')
    enrollment_date = fields.Date('注册时间')
    employee_num = fields.Integer('员工总数')
    corporation_name = fields.Char('法人姓名')
    client_product = fields.Char('客户产品')
    client_description = fields.Text('客户简介')
    crm_level = fields.Selection(
        [('no', '不太关注'), ('little', '一般关注'), ('some', '重点关注')],
        string='关注级别')

    crm_financial_code = fields.Char(string='纳税人识别号')
    crm_financial_bank = fields.Char('开户行')
    crm_financial_username = fields.Char('账号')
    crm_financial_phone = fields.Char('财务电话')

    crm_address_code = fields.Char('邮政编码')
    crm_address_place = fields.Char('省/市/自治区')
    crm_address_city = fields.Char('城市')
    crm_address = fields.Char('单位地址')
    crm_communicate_address = fields.Char('通讯地址')

    def open_business_form_view(self):
        return {
            'name': 'Model ',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'form',

            'view': self.env.ref('crm.crm_lead_view_form').id,
            'context': {'default_partner_id': self.id},

        }

    def open_analysis_form_view(self):
        return {
            'name': 'Model ',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'form',

            'view': self.env.ref('crm.crm_lead_view_form').id,
            'context': {'default_partner_id': self.id},
        }

    def open_dashboard_form_view(self):
        return {
            'name': 'Model ',
            'type': 'ir.actions.act_window',
            'res_model': 'board.board',
            'view_mode': 'form',
            'view': self.env.ref('dashboard_form_view').id,

        }

