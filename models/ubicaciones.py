from odoo import fields, models, api


class HospitalUbicaciones(models.Model):
    _name = 'hospital.ubicaciones'
    _description = 'Lista de Ubicaciones'

    name = fields.Char("Ubicacion")
    area = fields.Char("Area")

    responsable = fields.Many2one('res.partner', "Responsable")