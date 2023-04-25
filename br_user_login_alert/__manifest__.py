
{
    'name': 'Br User Login Alert',
    'summary': """User Login Notices.""",
    'version': '16.0.1.0.0',
    'description': """Secure your Odoo account by alerts at right time. If any successful login to your
                    account happens, an alert mail will be send to you with the browser and IP details, Odoo 16, Odoo16""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'category': 'Tools',
    'depends': ['base', 'mail'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'data': [
        'security/notification_group.xml',
        'views/logged_details_view.xml',
    ],
    'images': ['static/description/banner.png',
              'static/description/icon.png',],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': ['httpagentparser'],
    },
}

