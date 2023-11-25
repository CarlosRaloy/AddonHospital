from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'hospital.especialidades'
    _description = 'Especialidades del hospital'

    name = fields.Char()
    codigo = fields.Char()
    descripcion = fields.Char()

