from odoo import fields, models, api


class HospitalConsultorio(models.Model):
    _name = 'hospital.consultorio'
    _description = 'Son los consultorios del hospital'

    name = fields.Char("Consultorio")
    doctor = fields.Many2one('hospital.doctores', 'Doctores')
    especialidad = fields.Many2one('hospital.especialidades', 'Especialidades')
    ubicacion = fields.Many2one('hospital.ubicaciones', 'Ubicaciones')
    horario = fields.Char("Horario")
