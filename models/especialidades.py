from odoo import fields, models, api


class HospitalEspecialidades(models.Model):
    _name = 'hospital.especialidades'
    _description = 'Especialidades del hospital'

    name = fields.Char()
    codigo = fields.Char()
    descripcion = fields.Char()

