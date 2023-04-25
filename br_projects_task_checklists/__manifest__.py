
{
    'name': 'Project Task Checklist',
    'version': '16.0.1.0.0',
    'category': 'Project/Project',
    'summary': "To Manage the Project's tasks, subtasks checklists",
    'description': "To Manage the Project's tasks, subtasks checklists",
    'author': 'Banibro IT Solutions Pvt Ltd.',
    'company': 'Banibro IT Solutions Pvt Ltd.',
    'website': 'https://banibro.com',
    'depends': ['project'],
    'data': [
        'security/ir.model.access.csv',
        'views/checklist_menu.xml',
        'views/checklist_add.xml',
    ],
    'assets': {
        'web.assets_backend': [
            "br_projects_task_checklists/static/src/js/progress.js",
        ],
    },
    'images': ['static/description/banner.png',
                'static/description/icon.png',],
    'license': 'AGPL-3',
    'email': "support@banibro.com",
    'installable': True,
    'application': False,
    'auto_install': False,
}
