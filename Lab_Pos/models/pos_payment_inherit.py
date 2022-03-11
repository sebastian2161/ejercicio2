# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class PosPayment01(models.Model):
    _inherit = 'pos.payment'
    
    importe_tipo_metodo = fields.Float(string='payment type amount', related='payment_method_id.importe_tipo_metodo', store=True)