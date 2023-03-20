{
    'name': "Offer Letter Creation",
    'version': "13.0",
    'price': 12.0,
    'currency': 'USD',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com/odoo-erp/',
    'summary': '''Offer letter creation for short listed employee''',
    'description': '''Offer letter creation for short listed employee''',
    'category': "hr",
    'depends': ['hr','hr_recruitment'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'data': [
            'security/ir.model.access.csv',
            'views/offer.xml',
            'data/offer_mail.xml',
             ],
    'images': ['static/description/banner.png',
               'static/description/icon.png',],
    'installable': True,
    'auto_install': False
}