

{
    'name': 'Product Custom Fields',
    'version': '16.0.1.0.0',
    'summary': """Ability To Add Custom Fields in Products From User Level""",
    'description': """Ability To Add Custom Fields in Products From User Level,Product Custom Fields,
                      Product Dynamic Fields, odoo15, Dynamic Product Fields, Dynamic Fields, Create Dynamic Fields, Community odoo Studio""",
    'category': 'Sales',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['product'],
    'data': [
        'data/widget_data.xml',
        'security/ir.model.access.csv',
        'security/product_security_group.xml',
        'wizard/product_fields_view.xml',
        'views/product_form_view.xml',
        'views/ir_fields_search_view.xml',
    ],
    'images': ['static/description/banner.png',
               'static/description/icon.png',],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,
}
