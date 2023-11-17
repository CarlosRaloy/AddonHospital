from odoo import fields, models, api


class HospitalAccount(models.Model):
    _inherit = 'account.move'

    hospital_id = fields.Many2one('hospital.registros', "Cita de registro")
