
{
    'name': "Sales and Purchase Price History for Products",
    'version': "13.0.0.0",
    'summary': "With the help of this module, You can find the rate which you have given to that customers/suppliers in past for that product.",
    'category': 'Sales',
    'description': """ You can use this module to retrieve the rate you've already charged certain clients or suppliers for that product.""",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['base', 'sale_management', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/inherited_product.xml',
        'views/inherited_res_config_setting.xml',
    ],
    'demo': [],
    "external_dependencies": {},
    "license": "AGPL-3",
    'email': "support@banibro.com",
    'installable': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
    "price": 0,
    "currency": 'EUR',
    
}
