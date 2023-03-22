
{
    'name': 'Product Brand Inventory',
    'version': '13.0.1.0.0',
    'category': 'Warehouse',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com/erp-software-company-in-chennai/',
    'summary': '''Brand of Goods in Inventory''',
    'description': '''Create product brand in inventory''',
    'images': ['static/description/banner.png',
               'static/description/icon.png',],
    'depends': ['stock'],
    'data': [
        'views/brand_views.xml',
        'security/ir.model.access.csv',
    ],
   'license': 'AGPL-3',
   'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,

}
