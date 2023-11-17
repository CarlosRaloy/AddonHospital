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
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/consultorio.xml'
        'views/registros.xml',
        ],
    'installable': True,
    'auto_install': False,
    'application': True
}

