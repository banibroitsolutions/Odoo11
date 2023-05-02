

{
    'name': 'Out Of Stock Products Restriction On Sales',
    'version': '16.0.1.0.0',
    'summary': 'Out Of Stock Products Restriction On Sales',
    'description': """Out Of Stock Products Restriction On Sales""",
    'category': 'Sales/Sales',
   'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['base', 'sale_management', 'stock', 'account'],
    'data': [
        'views/res_config_views.xml',
        'views/sale_order.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3',
    'email': "support@banibro.com",

}
