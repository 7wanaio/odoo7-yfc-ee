from odoo import api, fields, models


class SchoolSchool(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char('姓名', store=True)
    value = fields.Integer('成绩', store=True)

