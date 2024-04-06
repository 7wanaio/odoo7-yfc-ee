# -*- coding: utf-8 -*-

from odoo import models, fields, api


class develop_list(models.Model):
    _name = 'develop_list.develop_list'
    _description = 'develop_list.develop_list'

    type_by = fields.Many2one('unit.model', '归属型号')
    contract_name = fields.Char('项目名称')
    contract_time = fields.Date('项目年份')
    contract_code = fields.Char('项目编号')
    capital_type = fields.Char('资金类型')
    sum_capital = fields.Integer("项目金额")
    contract_margins = fields.Integer('利润')
    Our_Company = fields.Many2one('res.partner', '甲方单位')
    other_company = fields.Many2one('res.partner', '乙方单位')
    accounts_receivable = fields.Integer('待收款项')
    capital_speed = fields.Selection([('not', '未打款'), ('half', '已有部分打款'), ('finish', '已完结')],
                                     default='not',
                                     string='资金进度')
    receipt_speed = fields.Selection([('not', '未报销'), ('half', '已有部分报销'), ('finish', '已完结')],
                                     default='not',
                                     string='发票进度')

    def develop_open_business_form_view(self):
        return {
            'name': 'Model ',
            'type': 'ir.actions.act_window',
            'res_model': 'crm.lead',
            'view_mode': 'form',
            'view': self.env.ref('crm.crm_lead_view_form').id,
        }

class unitmodel(models.Model):
    _name = 'unit.model'

    name = fields.Char('型号')
    unit_description = fields.Char('型号描述')
