# -*- coding: utf-8 -*-


{
    'name': "Sale Reminder",
    'version': "11.0.1.0.0",
    'author': 'Banibro',
    'company': 'Banibro IT Solutions',
    'website': 'https://www.banibro.com',
    'summary': '''Automatically send email to manager on saving the sale quotation''',
    'description': '''Automatically send email to manager on saving the sale quotation''',
    'category': "Sale",
    'depends': ['sale'],
    'license': 'AGPL-3',
    'data': [
            'views/sale_email_reminder.xml',
            'views/sale_change_view_email.xml',
            'data/sale_change_action_data.xml'
             ],
    'demo': [],
    'images': [],
    'installable': True,
    'auto_install': False
}
