# -*- coding: utf-8 -*-

from odoo import models, fields, api


class order_demo(models.Model):
    _name = 'order_demo.order_demo'
    _description = 'order_demo.order_demo'

    name = fields.Char()

    order_name = fields.Char('订单名称')
    order_code = fields.Char('订单编号')
    production_code = fields.Char('投产编号')
    production_date = fields.Date('订购日期')
    production_unit = fields.Char('投产型号')
    apply_unit = fields.Char('投产型号')
    production_purchase = fields.Char('订购单位')
    production_accept = fields.Char('收货单位')
    buy_unit = fields.Many2one('res.partner','订购单位')
    get_unit = fields.Many2one('res.partner','收货单位')
    army = fields.Char('军检')
    is_free = fields.Selection([('yes', '是'), ('no', '否')], '是否收费')
    put_product_ids = fields.One2many('products.message', 'put_product_id', '进度计划')


class ProductsMessage(models.Model):
    _name = 'products.message'
    _description = ''

    name = fields.Char('')
    put_product_id = fields.Many2one('order_demo.order_demo')

    product_name = fields.Char('产品名称')
    product_code = fields.Char('产品编号')
    product_step = fields.Char('阶段')
    task_code = fields.Char('任务号')
    unit = fields.Char('单位')
    purchase_date = fields.Date('订购时间')
    submit_date = fields.Date('交付时间')
    two_submit_date = fields.Date('调整后交付时间')
