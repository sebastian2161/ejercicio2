# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PosPayment01(models.Model):
    _inherit = 'pos.order'
    
    tipo_metodo_id = fields.Many2one(comodel_name='pos.payment.method',string='Related Tipo Metodo',ondelete='set null')
        
    importe_tipo_metodo = fields.Float(string='tipo metodo', related='tipo_metodo_id.importe_tipo_metodo')