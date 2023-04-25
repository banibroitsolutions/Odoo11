
{
    'name': 'Payment Approvals',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': """ This modules enables approval feature in the payment.""",
    'description': """This modules enables approval feature in the payment. """,
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['base', 'account'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/account_payment_view.xml',
    ],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'images': ['static/description/banner.png',
               'static/description/icon.png',],
    'installable': True,
    'auto_install': False,
    'application': True,
}
