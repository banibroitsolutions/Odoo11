

{
    'name': "Purchase Order Multi Product Selection",
    'version': "13.0.0.1",
    'summary': "This module allows you to select Multiple product in purchase order at a time on single click.",
    'category': 'Purchases',
    'description': """
        This module enables you to choose multiple products from an order with only one click.""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['base', 'purchase', 'product'],
    'data': [
                'security/ir.model.access.csv',
        'views/purchase.xml',
        'views/product.xml'
    ],
    'demo': [],
    "license": "AGPL-3",
    'email': "support@banibro.com",
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
