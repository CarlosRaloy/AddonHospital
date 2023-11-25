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
    color = fields.Integer('Color')

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

    def _get_to_date(self):
        date = self.date
        return date.strftime('%d') + " de " + self.get_mes(date.strftime('%m')) + " de " + date.strftime('%Y')


    def get_mes(self, n=1):
        if n == 1:
            return 'Enero'
        elif n == 2:
            return 'Febrero'
        elif n == 3:
            return 'Marzo'
        elif n == 4:
            return 'Abril'
        elif n == 5:
            return 'Mayo'
        elif n == 6:
            return 'Junio'
        elif n == 7:
            return 'Julio'
        elif n == 8:
            return 'Agosto'
        elif n == 9:
            return 'Septiembre'
        elif n == 10:
            return 'Octubre'
        elif n == 11:
            return 'Noviembre'
        elif n == 12:
            return 'Diciembre'


    @api.model
    def create(self, vals):
        # raise UserError(_(vals))
        if vals['state'] == '1':
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.registros')
        result = super(HospitalRegistros, self).create(vals)
        return result


    def imprimir_reporte(self):
        for res in self:
            data={
                "docs": res,
                "saludo":"Hola Mundo"
            }
            return self.env.ref('hospital.report_hospital_registros').report_action(self, data=data)

    # Apply in operations fields, your action is on save changes
    @api.depends('peso','time_out')
    def prueba_depends(self):
        return False

    # Is more restrictive, Is Functional with the user
    @api.onchange('peso','time_out')
    def prueba_onchange(self):
        return False

    def ejemplo_botton(self):
        raise UserError(_('Hola Mundo'))
