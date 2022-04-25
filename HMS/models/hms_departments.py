from odoo import models, fields


class Departments(models.Model):
    _name = 'hms.departments'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()


    patients_ids = fields.Many2one('hms', 'dept_no')





