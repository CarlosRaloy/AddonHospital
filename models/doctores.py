from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'hospital.doctores'
    _description = 'son los doctores del hospital'

    name = fields.Char()
    edad = fields.Integer()
    cedula = fields.Char()
