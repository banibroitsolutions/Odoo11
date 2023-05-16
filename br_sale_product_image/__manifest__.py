
{
    "name": "Br Sale Order Line Images",
    "summary": "Order Line Images from the Sale and Sale Report",
    "version": "16.0.1.0.0",
    "category": 'Sales',
    "description": """Order Line Images In Sale and Sale Report, odoo 16, order line images""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    "depends": [
        'sale_management',
    ],
    "data": [
        'views/sale_order_line_image.xml',
        'views/res_config_settings.xml',
        'report/sale_order_report.xml',
    ],
    'images': ['static/description/banner.png',
               'static/description/icon.png',],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,
}
