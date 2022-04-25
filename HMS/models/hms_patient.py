from odoo import models, fields, api

from odoo.exceptions import ValidationError, UserError
import re

from datetime import date

class Patient(models.Model):
    _name = 'hms.patient'

    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    history = fields.Char()
    CR_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O'),
    ])
    pcr = fields.Boolean()
    image = fields.Image()
    address = fields.Text()
    age = fields.Integer()
    e_mail = fields.Char()

    dept_ids = fields.Many2one('hms.departments')
    history_ids = fields.Many2one('hms.history')


    drs_ids = fields.Many2many(comodel_name='hms.doctors')

    capacity = fields.Integer(related='dept_ids.capacity')

    @api.onchange('age')
    def check_age(self):
        for rec in self:
            if rec.age <= 30:
                self.pcr = True
                return {
                    'warning': {
                        'title': 'PCR',
                        'message': 'pcr has been checked.'
                    }
                }

    # def first_state(self):
    #     self.state = 'Undetermined'
    #     history = self.env['hms.history'].create({
    #         'my_date': date.today(),
    #         'description': 'this is a description',
    #
    #     })
    # def second_state(self):
    #     self.state = 'Good'
    #     history = self.env['hms.history'].create({
    #         'my_date': date.today(),
    #         'description': 'this is a description',
    #
    #     })
    # def third_state(self):
    #     self.state = 'Fair'
    #     history = self.env['hms.history'].create({
    #         'my_date': date.today(),
    #         'description': 'this is a description',
    #
    #     })
    # def fourth_state(self):
    #     self.state = 'Serious'
    #     history = self.env['hms.history'].create({
    #         'my_date': date.today(),
    #         'description': 'this is a description',

        # })

    state = fields.Selection([
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious)'),

    ], default='Undetermined')

    # def first_state(self):
    #     self.state = 'Undetermined'

    # def second_state(self):
    #     self.state = 'Good'

    # def third_state(self):
    #     self.state = 'Fair'

    # def fourth_state(self):
    #     self.state = 'Serious'



    # def validate(self):
    #     if self.e_mail:
    #         match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.e_mail)
    #         if match == None:
    #             raise UserError("invalid e-mail")



    @api.onchange('birth_date')
    def _onchange_birth_date(self):
        if self.birth_date:
            self.age = date.today().year - self.birth_date.year

    @api.onchange('Email')
    def validate_mail(self):
        if self.Email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.Email)
            if match == None:

                raise ValidationError('Not a valid E-mail ')

    def create_log(self):

        self.env['hms.log.history'].create({
            'created_by': self.First_name,
            'Date': date.today(),
            'Description': f'State changed to {self.state} ',
            'patient_id': self.id
        })

    def next_stage(self):
        if self.state == 'undetermined':
            self.state = 'good'
        elif self.state == 'good':
            self.state = 'fair'
        elif self.state == 'fair':
            self.state = 'serious'
        elif self.state == 'serious':
            self.state = 'undetermined'
        self.create_log()