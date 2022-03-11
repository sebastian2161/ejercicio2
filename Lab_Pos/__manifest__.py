# Copyright 2022 SNC-SOFT SOLUTIONS - Sebastian Collao
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': 'Lab Pos',
    'summary': """Lab Pos""",
    'description': """
        Lab Pos module to manage training:
         -Point of Sales
         
     """,
    
    'author': 'SNC-SOFT SOLUTIONS',
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    'website': 'https://www.snc-soft.com/',
    'category': 'Pos type Payments',
    'version': '0.1',
    'depends': ['point_of_sale'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        #'views/sale_views_inherit.xml',
        #'views/product_views_inherit.xml',
        #'wizard/sale_wizard_view.xml',
        #'report/session_report_template.xml',
        #'views/prueba_web.xml',
        #'views/academy_course_controllers.xml',
        #'views/todo_templates.xml',
        #'views/todo_extend.xml',
        #'views/todo_web.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    
}

