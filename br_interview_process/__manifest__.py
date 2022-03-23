{
    'name': "Interview Request Creation",
    'version': "13.0",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://www.banibro.com',
    'summary': '''Interview Request creation for Applicant''',
    'description': '''interview request creation for applicant''',
    'category': "hr",
    'depends': ['hr','hr_recruitment','mail'],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'data': [
            'security/ir.model.access.csv',
            'views/interview.xml',
            'data/interview_report.xml',
             ],
    'images': ['static/description/banner.png'],         
    'installable': True,
    'auto_install': False,
    'price': 80,
    'currency': 'USD'
    
}