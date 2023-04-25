

{
    'name': 'Generate QR Codes for Customer and Products',
    'version': '16.0.1.0.0',
    'summary': '''Develop the Unique QR Codes for Customers and Products''',
    'description': '''QR Code, QR Code Generator, Odoo QR Code Generator, Customer QR Code, Product QR Code, QR, QR Code Odoo''',
    'category': 'Extra Tools',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['base', 'sale', 'stock'],
    'data': [
        'report/paperformat.xml',
        'report/report.xml',
        'views/view.xml',
        'report/template.xml',
    ],
    'images': ['static/description/banner.png',],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'post_init_hook': '_set_qr'
}
