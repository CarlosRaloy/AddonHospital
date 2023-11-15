from odoo import fields,models,api

class HospitalRegistros(models.Model):
    _name = 'hospital.registros'
    _descripcion = 'Registros de los pacientes que ingresan a consultorio'

    name = fields.Char("Clave de registro")
    partner_id = fields.Many2one('res.partner', "Paciente")
    date = fields.Datetime("Fecha de registro")
    date_in = fields.Datetime("Fecha de Ingreso")
    motive = fields.Text("Motivo de visita") 
    
    peso = fields.Float("Peso corporal en KG")
    time_out = fields.Float("Hora de salida")
