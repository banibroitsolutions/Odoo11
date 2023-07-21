# -*- coding: utf-8 -*-
{
    'name': 'Customized Bracode Generator',
    'version': '13.0.1.0.0',
    'summary': """Print user defined product labels.""",
    'description': """The module enables user to print customized product labels.
                    """,
    'category': 'Tools',
   'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com/odoo-for-manufacturing-company/',
    'depends': ['base', 'web', 'product','account'],
    'data': [
        'report/product_label_template.xml',
        'views/barcode_generator_view.xml',
        'security/ir.model.access.csv'
    ],
    'qweb': [],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,
}
