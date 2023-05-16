

{
    'name': 'Product Image from URL',
    'summary': 'Product Images from Web URL and Path',
    'version': '13.0.1.0.0',
    'description': """Product Images from Web URL, Product Images from path, local""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'category': 'Sales',
    'images': ['static/description/banner.png'],
    'depends': ['sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_url.xml',
        'wizard/product_import.xml',
    ],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'application': False,
    'auto_install': False,
}
