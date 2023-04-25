

{
    'name': "Customer Sequence",
    'version': '16.0.1.0.0',
    'summary': """Unique Customer Code""",
    'description': """
       Each customer have unique number code, Odoo 13, Odoo
    """,
     'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'category': 'Sales',
    'depends': ['sale_management'],
    'data': [
        'views/res_partner_fom.xml',
        'views/res_company.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.png',
                'static/description/icon.png',],
     'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'application': False
}
