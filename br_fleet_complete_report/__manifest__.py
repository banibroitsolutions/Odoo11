

{
    'name': 'Fleet - Complete Report',
    'version': '14.0.1.0.0',
    'category': 'Human Resources/Fleet',
    'summary': 'Custom report for Fleet',
    'description': 'Create complete PDF report for Fleet',
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'fleet'],
    'data': [
        'security/ir.model.access.csv',
        'report/vehicle_detail_report_templates.xml',
        'report/vehicle_detail_reports.xml',
        'wizard/vehicle_detail_views.xml'
    ],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,
}
