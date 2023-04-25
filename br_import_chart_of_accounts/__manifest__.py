# -*- coding: utf-8 -*-
{
	'name': 'Import Chart of Accounts from CSV or Excel File',	
	'version': '16.0.0.2',
	'category': 'Accounting',
	'summary': 'This apps helps to import chart of accounts using CSV or Excel file',
	'description': '''Using this module Charts os accounts is imported using excel sheets
	import accounts using csv 
	import accounts using xls
	import accounts using excel
	import Chart of account using csv 
	import Chart of account using xls
	import chart of accounts using excel
	import COA using csv 
	import COA using xls
	import COA using excel
	''',
	'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
	'depends': ['base','account'],
	'license': 'AGPL-3',
    'email': "support@banibro.com",
	'data': [
		'security/ir.model.access.csv',
		'wizard/view_import_chart.xml',
		],
	'auto_install': False,
	'installable': True,
    	'application': True,
    	'qweb': [
    		],
   	'images': ['static/description/banner.png',
               'static/description/icon.png',],
}

