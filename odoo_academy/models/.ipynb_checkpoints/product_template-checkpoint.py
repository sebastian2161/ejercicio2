# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_ssesion_product = fields.Boolean(string='Use as Session Product',
                                        help='Check this box to use it',
                                        default=False)
    