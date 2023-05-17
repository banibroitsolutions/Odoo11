
{
    "name": "Odoo13 CRM Commission Plan",
    'description': """CRM Commission Plan for odoo13, CRM, crm commission, commission plan, crm features""",
    'summary': """CRM Commission Plan for odoo13""",
    "category": 'Sales',
    "version": '13.0.1.0.0',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    "depends": ['base', 'sale_management', 'crm'],
    "data": [
        'security/ir.model.access.csv',
        'views/commission.xml',
        'wizard/commission_report.xml',
        'views/action_manager.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'license': 'LGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'application': False,
    'auto_install': False,
}
