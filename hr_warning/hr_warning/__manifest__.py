# -*- coding: utf-8 -*-
{
    'name': "hr_warning",

    'summary': """
        This service helps to Manage Violation Warnings and Termination details of respective Employees. Regular Reminders as well as Follow-ups can be set.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Banibro IT Solutions Pvt Ltd.",
    'website': "http://www.banibro.com",
	'license': "AGPL-3",
	'email': "support@banibro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':'hr',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_resignation'],

    # always loaded
    'data': ['security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'wizard/second_warning.xml',
        'views/templates.xml',
        # 'data/fire.xml',
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['hr_warning/static/description/icon.png'],  
    'installable': True,
    'auto_install': False,
	'price': 18,
    'currency': 'USD'
}
