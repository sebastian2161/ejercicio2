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
    'website': 'https://www.snc-soft.com/',
    'category': 'Pos type Payments',
    'version': '0.1',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_payment_method_inherit.xml',
        'views/pos_payment_inherit.xml',
        
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

