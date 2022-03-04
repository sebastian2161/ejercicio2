# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PosPaymentMethod01(models.Model):
    _inherit = 'pos.payment.method'
    
    importe_tipo_metodo = fields.Float(string='importe tipo metodo', default=0.00, required=True, help="Total tipos de metodo")
    
    