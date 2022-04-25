from odoo import models, fields
from datetime import date




class History(models.Model):
    _name = 'hms.log.history'
    _rec_name = 'created_by'

    created_by = fields.Char()
    Date = fields.Date()
    Description = fields.Text()
    patient_id = fields.Many2one('hms.patient')


    patient_ids = fields.One2many('hms.patient', 'history_ids')
