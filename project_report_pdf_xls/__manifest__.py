

{
    'name': "Project Report XLS and PDF",
    'version': "13.0",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com/erp-software-company-in-chennai/',
    'summary': '''Effective PDF & XLS Reports with Filtrations for Project''',
    'description': '''Project With Filtrations, Enhanced PDF & XLS Reports, Odoo 13''',
    'category': "Project",
    'depends': ['base', 'project'],
    'data': ['views/action_manager.xml',
             'wizard/project_report_wizard_view.xml',
             'report/project_report_pdf_view.xml',
             'views/project_report_button.xml',
             'views/project_report.xml'
             ],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'images': ['static/description/banner.png',
               'static/description/icon.png',  ],
    'installable': True,
    'auto_install': False,
}
