

{
    'name': "Product Catalogue",
    'version': '13.0.1.0.0',
    'summary': """This module helps to print the catalogue of
                the single/multi products from the backend and single product its variants
                from the E-commerce website
                including details like images and specifications""",
    'description': """This module helps to print the catalogue of
                the single/multi products from the backend and single product and its variants
                from the E-commerce website
                including details like images and specifications""",
    'category': 'Inventory',
   'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'sequence': 1,
    'depends': ['base', 'stock', 'website_sale'],
    'data': [
        'views/report_button_website.xml',
        'report/product_catalog_report.xml',
        'report/product_catalog_template.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'email': "support@banibro.com",
    'installable': True,
    'application': False,
}
