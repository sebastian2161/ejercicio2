# -*- coding: utf-8 -*-

{
    'name': 'viaje Espacial Odoo',
    'summary': """Organizacion de logistica Mision Espacial""",
    'description': """
        Organizacion de logistica Mision Espacial:
         -Nave Espacial
         -Tripulacion
     """,
    
    'author': 'seba01',
    'website': 'https://www.odoo.com/',
    'category': 'Espacial',
    'version': '0.1',
    'depends': ['base','project'],
    'data': [
        'security/nave_security.xml',
        'security/ir.model.access.csv',
        'views/nave_menuitems.xml',
        'views/nave_view.xml',
        'views/mision_view.xml',
        'views/project_views_inherit.xml',
        'wizard/project_wizard_view.xml',
    ],
    'demo': [
        'demo/mision_espacial.xml',
    ],
    
    
}