# -*- coding: utf-8 -*-

from odoo import fields, models


class CrmNew(models.Model):
    _inherit = 'crm.lead'

    item_name = fields.Text('项目名称')
    get_time = fields.Date('获取时间')

    get_routine = fields.Selection(
        [('one', '开发计划'), ('two', '自主开发'), ('three', '自主获取'), ('four', '领导分配'), ('five', '他人介绍')],
        string='获取渠道')
    item_type = fields.Selection(
        [('one', '弹体列装'), ('two', '研制保障'), ('three', '装备保障'), ('four', '地面猎装')],
        string='项目类别')
    model_name = fields.Char(string='型号')
    technique_ids = fields.One2many('technique.decision', 'technique_id', '技术决策链')
    business_ids = fields.One2many('business.decision', 'business_id', '商务决策链')
    governor_satisfy = fields.Selection(
        [('one', '非常支持'), ('two', '比较认可'), ('three', '仅限了解'), ('four', '不太关注'), ('five', '可以改善'),
         ('six', '比较疏远'), ('seven', '坚决否定')], string='最高决策层')
    client_type = fields.Selection(
        [('strategic', '战略客户'), ('common', '普通客户'), ('potential_strategic', '潜在战略客户'),
         ('potential', '潜在客户'), ('importance', '重要客户')], default='common',
        string='客户类型')
    contribute_degree = fields.Selection(
        [('one', '暂无合同'), ('two', '年合同额100万以下'), ('three', '年合同额100-300万'),
         ('four', '年合同额300-500万'), ('five', '年合同额500万以上'),
         ], string='贡献程度')
    account_degree = fields.Selection(
        [('one', '回款困难'), ('two', '完全不按合同执行'), ('three', '略拖延'),
         ('four', '按合同履约')
         ], string='回款难度')
    model_step = fields.Selection(
        [('one', '项目意向阶段'), ('two', '项目需求调研'), ('three', '项目可研论证'),
         ('four', '项目立项申报'), ('five', '项目立项批复'), ('six', '项目方案论证'), ('seven', '项目投标阶段')
         ], string='型号阶段')
    model_description = fields.Text('型号介绍')
    item_description = fields.Text('项目简述')
    progress_ids = fields.One2many('progress.plan', 'progress_id', '进度计划')
    list_ids = fields.One2many('list.description', 'list_id', '工作计划')
    capital_category = fields.Selection([
        ('electronics', '国家政府专项'),
        ('books', '军方列装'),
        ('clothing', '保障装备'), ('one', '技改技措'), ('two', '预研课题'), ('three', '申报课题'),
        ('four', '自筹建设正在筹措')
    ], string='资金渠道')
    capital_situation_category = fields.Selection([
        ('electronics', '已到位'),
        ('books', '部分到位'),
        ('clothing', '其他'), ('clothing', '待批复'), ('clothing', '正申报'), ('clothing', '正计划')
    ], string='资金情况')

    capital_first_category = fields.Selection([
        ('electronics', '500万以下'),
        ('books', '500-1000万'),
        ('clothing', '1000万以上'),
    ], string='项目预算')

    capital_all_category = fields.Selection([
        ('electronics', '500万以下'),
        ('books', '500-1000万'),
        ('clothing', '1000万-2000万'), ('one', '2000万以上'),
    ], string='全周期项目预算')

    limit_category = fields.Selection([
        ('electronics', '有限制'),
        ('books', '严格无限制'),
        ('clothing', '无限制'),
    ], string='资质限制')

    compete_category = fields.Selection([
        ('electronics', '直接采购无竞争'),
        ('books', '直接采购有1家竞争'),
        ('clothing', '联合研制有1家竞争'), ('clothing', '内部招标三家'), ('clothing', '内部招标三家以上'),
        ('clothing', '公开招标三家竞争'), ('clothing', '公开招标三家以上竞争'),
    ], string='竞争对手')

    technique_category = fields.Selection([
        ('electronics', '项目表述不清晰'),
        ('books', '一般'),
        ('clothing', '项目表述清晰'),
    ], string='技术要求')
    technique_difficult_category = fields.Selection([
        ('electronics', '较为复杂'),
        ('books', '一般'),
        ('clothing', '简单'),
    ], string='技术难点')
    item_type_category = fields.Selection([
        ('electronics', '交付任务'),
        ('books', '方案任务'),
        ('clothing', '其他'),
    ], string='项目类型')

    def open_order_form_view(self):
        return {
            'name': 'Model ',
            'type': 'ir.actions.act_window',
            'res_model': 'order_demo.order_demo',
            'view_mode': 'form',

            'view': self.env.ref('order_demo.form').id,
            'context': {'default_production_unit': self.model_name, 'default_buy_unit': self.partner_id.id,
                        'default_get_unit': self.partner_id.id},

        }


class TechniqueDecision(models.Model):
    _name = 'technique.decision'
    _description = ''

    name = fields.Char('')
    technique_id = fields.Many2one('crm.lead')

    technique_supervisor_satisfy = fields.Selection(
        [('one', '非常支持'), ('two', '比较认可'), ('three', '仅限了解'), ('four', '不太关注'), ('five', '可以改善'),
         ('six', '比较疏远'), ('seven', '坚决否定')], string='主管')
    technique_head_satisfy = fields.Selection(
        [('one', '非常支持'), ('two', '比较认可'), ('three', '仅限了解'), ('four', '不太关注'), ('five', '可以改善'),
         ('six', '比较疏远'), ('seven', '坚决否定')], string='主任')
    technique_governor_satisfy = fields.Selection(
        [('one', '非常支持'), ('two', '比较认可'), ('three', '仅限了解'), ('four', '不太关注'), ('five', '可以改善'),
         ('six', '比较疏远'), ('seven', '坚决否定')], string='型号总')


class BusinessDecision(models.Model):
    _name = 'business.decision'
    _description = ''

    name = fields.Char('')
    business_id = fields.Many2one('crm.lead')

    business_supervisor_satisfy = fields.Selection(
        [('one', '非常支持'), ('two', '比较认可'), ('three', '仅限了解'), ('four', '不太关注'), ('five', '可以改善'),
         ('six', '比较疏远'), ('seven', '坚决否定')], string='主管')
    business_head_satisfy = fields.Selection(
        [('one', '非常支持'), ('two', '比较认可'), ('three', '仅限了解'), ('four', '不太关注'), ('five', '可以改善'),
         ('six', '比较疏远'), ('seven', '坚决否定')], string='主任')
    business_governor_satisfy = fields.Selection(
        [('one', '非常支持'), ('two', '比较认可'), ('three', '仅限了解'), ('four', '不太关注'), ('five', '可以改善'),
         ('six', '比较疏远'), ('seven', '坚决否定')], string='型号总')


class ProgressPlan(models.Model):
    _name = 'progress.plan'
    _description = ''

    name = fields.Char('')
    progress_id = fields.Many2one('crm.lead')

    plan_name = fields.Char('项目计划')
    plan_time = fields.Date('计划节点')
    plan_number = fields.Integer('数量')
    plan_unit = fields.Char('单位')
    plan_content = fields.Char('备注')


class ListDescription(models.Model):
    _name = 'list.description'
    _description = ''

    name = fields.Char('')
    list_id = fields.Many2one('crm.lead')

    list_description = fields.Char('任务描述')
    list_time = fields.Date('完成时间')
    list_change_time = fields.Date('调整时间')
    list_change_num = fields.Integer('累计调整次数')
    task_goal = fields.Char('任务目标')
    duty_department = fields.Char('责任部门')
    duty_person = fields.Char('责任人')
