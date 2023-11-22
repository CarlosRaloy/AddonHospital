{
    'name': 'The Hospital Odoo',
    'version': '1.0',
    'description': 'Module At hospital',
    'category': 'Other',
    'author': 'Carlos Garcia Garcia',
    'website': 'python.org',
    'license': 'OPL-1',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',  # First is the security
        'data/secuencias.xml',  # Next to security or end of file
        'views/registros.xml',
        'views/consultorio.xml',
        #'views/doctores.xml',
        'views/menu.xml',  # The rule is the last menu
    ],
    'installable': True,
    'auto_install': False,
    'application': True
}
