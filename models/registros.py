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

    gravedad = fields.Selection([
        ('1','Baja'),
        ('2','Media'),
        ('3','Alta'),
    ],"Gravedad")

    state = fields.Selection([
        ('1','Sin Atender'),
        ('2','En revision (Consulta)'),
        ('3','Atendido'),
        
    ],"Estatus")

    # Forma de relacionar los id's entre modelos
    account_ids = fields.One2many('account.move', 'hospital_id', 'Facturas')