

{
    'name': 'BR Insurance Management',
    'version': '13.0.1.0.0',
    'summary': """Insurance Management & Operations""",
    'description': """Insurance Management""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'category': 'Industries',
    'depends': ['base', 'account'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'data': [
        'views/insurance_details.xml',
        'views/claim_details.xml',
        'views/employee_details.xml',
        'views/policy_management.xml',
        'views/insurance_sequence.xml',
        'views/insurance_management.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

