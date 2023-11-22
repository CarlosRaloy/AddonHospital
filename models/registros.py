from odoo import fields, models, api, _
from odoo.exceptions import UserError


class HospitalRegistros(models.Model):
    _name = 'hospital.registros'
    _descripcion = 'Registros de los pacientes que ingresan a consultorio'

    name = fields.Char("Clave de registro", default="/")
    partner_id = fields.Many2one('res.partner', "Paciente")
    date = fields.Datetime("Fecha de registro")
    date_in = fields.Datetime("Fecha de Ingreso")
    motive = fields.Text("Motivo de visita")

    peso = fields.Float("Peso corporal en KG")
    time_out = fields.Float("Hora de salida")

    gravedad = fields.Selection([
        ('1', 'Baja'),
        ('2', 'Media'),
        ('3', 'Alta'),
    ], "Gravedad")

    state = fields.Selection([
        ('1', 'Sin Atender'),
        ('2', 'En revision (Consulta)'),
        ('3', 'Atendido'),

    ], "Estatus", default='1')

    # Forma de relacionar los id's entre modelos
    account_ids = fields.One2many('account.move', 'hospital_id', 'Facturas')
    company_id = fields.Many2one('res.company', 'Compania', readonly=True,
                                 default=lambda self: self.env.company)

    # company_id = fields.Many2one('res.company', 'Compania', readonly=True,
    #                             default = lambda self: self.env['res.company']._

    @api.model
    def create(self, vals):
        # raise UserError(_(vals))
        if vals['state'] == '1':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.registros')
        result = super(HospitalRegistros, self).create(vals)
        return result

    # Apply in operations fields, your action is on save changes
    @api.depends('peso','time_out')
    def prueba_depends(self):
        return False

    # Is more restrictive, Is Functional with the user
    @api.onchange('peso','time_out')
    def prueba_onchange(self):
        return False
