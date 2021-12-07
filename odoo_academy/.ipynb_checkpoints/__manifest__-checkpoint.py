# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage training""",
    'description': """
        Academy module to manage training:
         -courses
         -sessions
         -attendes
     """,
    
    'author': 'seba',
    'website': 'https://www.odoo.com/',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale','website'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_template.xml',
        'views/prueba_web.xml',
        'views/academy_course_controllers.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    
}

# Manifiesto de hoy 20-09-2021
# Manifiesto de hoy 25-09-2021
# Manifiesto de hoy 27-09-2021
# Manifiesto de hoy 29-09-2021
# Manifiesto de hoy 29-09-2021
# Manifiesto de hoy 29-09-2021
# Manifiesto de hoy 29-09-2021
# Manifiesto de hoy 05-10-2021
# Manifiesto de hoy 07-10-2021
# Manifiesto de hoy 09-10-2021
# Manifiesto de hoy 11-10-2021
# Manifiesto de hoy 13-10-2021
# Manifiesto de hoy 15-10-2021
# Manifiesto de hoy 17-10-2021
# Manifiesto de hoy 19-10-2021
# Manifiesto de hoy 21-10-2021
# Manifiesto de hoy 21-10-2021
# Manifiesto de hoy 23-10-2021
# Manifiesto de hoy 24-10-2021
# Manifiesto de hoy 25-10-2021
# Manifiesto de hoy 28-10-2021
# Manifiesto de hoy 30-10-2021
# Manifiesto de hoy 30-10-2021
# Manifiesto de hoy 03-11-2021
# Manifiesto de hoy 05-11-2021
# Manifiesto de hoy 11-11-2021
# Manifiesto de hoy 11-11-2021
# Manifiesto de hoy 11-11-2021
# Manifiesto de hoy 12-11-2021
# Manifiesto de hoy 14-11-2021
# Manifiesto de hoy 14-11-2021
# Manifiesto de hoy 22-11-2021