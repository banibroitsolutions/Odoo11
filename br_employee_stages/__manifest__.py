

{
    'name': 'Employee Stages',
    'version': '13.0.1.0.0',
    'summary': """Manages Employee Stages""",
    'description': """This module is used to tracking employee's different stages.""",
    'category': "Generic Modules/Human Resources",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_stages_view.xml',
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,
}


