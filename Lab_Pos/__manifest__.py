# Copyright 2022 SNC-SOFT SOLUTIONS - Sebastian Collao
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': 'Transactional Amount - Payment Methods - POS',
    'summary': """Transactional Amount - Payment Methods - POS""",
    'description': """
        Lab Pos module to manage training:
         -Point of Sales
         
     """,
    
    'author': 'SNC-SOFT SOLUTIONS',
    "license": "LGPL-3",
    'website': 'https://www.snc-soft.com/',
    'category': 'Point of Sale',
    'version': '0.1',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_payment_method_inherit.xml',
        'views/pos_payment_inherit.xml',
        
    ],
    'demo': [
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}

