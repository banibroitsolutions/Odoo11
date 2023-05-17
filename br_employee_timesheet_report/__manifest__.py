
{
    'name': 'Br Timesheet PDF Report',
    'version': '13.0.1.0.0',
    "category": "Generic Modules/Human Resources",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com/erp-software-company-in-chennai/',
    'summary': '''PDF Report Timesheet of Employees''',
    'description': '''Print Timesheet PDF Report Of Employees''',
    'depends': ['hr_timesheet'],
    'data': [
             'report/report_timesheets.xml',
             'report/timesheet_pdf.xml',
             'wizard/timesheet_wizard.xml',
            ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'application': False,
}
