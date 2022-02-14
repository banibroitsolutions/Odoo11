{
    "name": "BR Timesheet report",
    "version": "13.0.1.0.0",
    "author": "Banibro IT Solutions Pvt Ltd.",
    "category": "project",
    "summary": '''Pending work on their Task list will receive Automatic Email reminders from Odoo Application daily.''',
    "license": "AGPL-3",
    "website": "https://www.banibro.com",
	'license': "AGPL-3",
	'email': "support@banibro.com",
    "depends": ["hr","hr_timesheet"],
    "data": [
        'views/timesheet_cr.xml',
    ],
    'images': ['br_timesheet_reminder/static/description/icon.png'],
    "auto_install": False,
    "installable": True,
	'price': 10,
    'currency': 'USD'
}
