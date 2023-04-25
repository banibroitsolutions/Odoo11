

{
    'name': 'Digital Signature In Purchase Order, Invoice, Inventory',
    'summary': 'Digital Signature in Purchase Order, Invoice, Inventory V16',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'description': """Digital Signature in Purchase Order, Invoice, Inventory V16""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['purchase', 'stock', 'account'],
    'data': [
        'views/res_config_settings.xml',
        'views/purchase_order.xml',
        'views/inventory.xml',
        'views/invoice.xml',
        'views/purchase_report_inherit.xml',
        'views/stock_picking_report.xml',
        'views/invoice_report.xml',
    ],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'application': False,
   'images': ['static/description/banner.png',
               'static/description/icon.png',],
   
}
