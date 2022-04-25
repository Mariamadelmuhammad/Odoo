{
    'name': 'HMS patient',
    'summary': 'Hospitals Management System',
    'depends': ['base', 'crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hms_views.xml',
        'views/hms_departments_views.xml',
        'views/hms_doctors_views.xml',
        'views/hms_log_history_views.xml',
        'views/crm_customer_views.xml',
        'reports/report.xml',
        'reports/template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}