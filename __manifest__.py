{
    'name': 'Employee Feedback',  # Name of the module
    'author':'Khaled Elaraby',
    'version': '17.0.0.1.0',  # Version of the module
    'category': 'Human Resources',  # Category for the module
    'depends': ['base', 'hr'],  # Dependencies
    'data': [
        'views/base_menu.xml',
        'views/form_view.xml',
        'views/tree_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml'

    ],
    'application': True
}
