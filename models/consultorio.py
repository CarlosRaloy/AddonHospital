from odoo import fields, models, api


class HospitalConsultorio(models.Model):
    _name = 'hospital.consultorio'
    _description = 'Son los consultorios del hospital'

    name = fields.Char("Consultorio")
    doctor = fields.Char("Doctor") # Modelo
    especialidad = fields.Char("Especialidad") # Modelo
    ubicacion = fields.Char("Ubicacion") # Modelo
    horario = fields.Char("Horario")
