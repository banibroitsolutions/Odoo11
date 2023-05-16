
{
    'name': "Sales History Of Products",
    'version': '13.0.1.0.0',
    'summary': """Sales history of products from Sales Order Line""",
    'description': """Sales history of products from Sales Order Line""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'category': 'Sales/Sales',
    'depends': ['base', 'sale_management'],
     'license': 'AGPL-3',
    'email': "support@banibro.com",
    'data': [
        'security/ir.model.access.csv',
        'wizard/sales_order_history_wizard_view.xml',
        'views/view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}
