# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PosPayment01(models.Model):
    _inherit = 'pos.payment'
    
    #payment_method_id01 = fields.Many2one(comodel_name='pos.payment.method', string='Related Tipo Pago', ondelete='set null')
    
    importe_tipo_metodo = fields.Float(string='importe tipo metodo', related='payment_method_id.importe_tipo_metodo')
    importe_prueba01 = fields.Monetary(string='importe 01', default=1, required=True,oldname='importe_tipo_metodo', help="Importe 01")
    
    
    
    
