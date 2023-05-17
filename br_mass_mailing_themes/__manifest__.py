# -*- coding: utf-8 -*-

{
    'name': 'Mass Mailing Theme (with color picker)',
    'summary': 'Send beautiful and mobile compatible emails with your brand colors. 60+ new mailing snippets. (Mass mailing theme, Mass mailing template, Massmailing theme, Email Template)',
    'description': """
        Send beautiful and mobile compatible mail with your brand colors (with color picker).""",

    'version': '13.0.0.5.1',
    'license': 'OPL-1',
    'email': "support@banibro.com",
    'category': 'Marketing',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',

    'depends': [
        'mass_mailing',
    ],
    'data': [
        'views/mass_mailing_themes_templates.xml',
        'views/assets.xml',
        'views/res_config_settings_views.xml',
        'views/s_generic_blocks.xml',
        'views/snippets.xml'
    ],

    "price": 153.50,
    "currency": "EUR",
    'qweb': ['static/src/xml/*.xml'],
    'images': ['static/description/images/banner.png'],
    'installable': True,
    'application': True
}
