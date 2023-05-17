# -*- coding: utf-8 -*-
{
    'name': "Modern Odoo Dashboards",

   'summary': """
       Dashboard - POS dashboard, CRM dashboard, inventory dashboard, sales dashboard in odoo, account dashboard in odoo with chart and graphs and table view.""",

    'depends': ['base','sale_management','crm','stock','account','point_of_sale',
    'hr_attendance'],


    'data': [
        'security/security.xml',
        'views/assets.xml',
        'views/sale_search_view.xml',
        'views/pos_config.xml',
        'views/account_search_view.xml',
        'views/crm_search_view.xml',
        'views/inventory_searcch_view.xml',
        'views/menu_dashboard_view.xml',
    ],

    'qweb': ["static/src/xml/sale_dashboard.xml",
             "static/src/xml/crm_dashboard.xml",
             "static/src/xml/inventory_dashboard.xml",
             "static/src/xml/account_dashboard.xml",
             "static/src/xml/sales_dashboard.xml",
             "static/src/xml/backend_dashboard.xml",
             ],
             
    'application': True,
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'price': 150,
    'currency': 'USD',
     'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'images': ['static/description/images/Banner-Img.png'],
}