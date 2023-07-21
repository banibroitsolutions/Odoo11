
{
    'name': 'Inter Company Stock Transfer',
    'version': '13.0.1.0.0',
    'summary': """Create counterpart Receipt/Delivery Orders between companies.""",
    'description': """Automatically Create Receipt/Delivery orders if any company validates a 
                      Deliver Order/Receipt to the selected company,Inter Company Stock Transfer, Stock Transfer,
                      Create counterpart Receipt/Delivery Orders between companies""",
    'category': 'Warehouse',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com/odoo-for-manufacturing-company/',
    'depends': ['stock', 'account'],
    'data': [
        'views/res_company_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,
}
