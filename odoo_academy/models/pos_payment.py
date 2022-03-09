# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class PosPayment01(models.Model):
    _inherit = 'pos.payment'
    
    #payment_method_id01 = fields.Many2one(comodel_name='pos.payment.method', string='Related Tipo Pago', ondelete='set null')
    #campo02 = fields.Float(string='campo02')
    #payment_method_id01 = fields.Many2one(comodel_name='pos.payment.method', string='importe_tipo_metodo', required=True)
    #tipo_pago01 = fields.Many2one(string='tipo_pago01',related='payment_method_id01.importe_tipo_metodo')
    
    importe_tipo_metodo = fields.Float(string='importe tipo metodo', related='payment_method_id.importe_tipo_metodo', store=True)
    #importe_prueba01 = fields.Monetary(string='importe 01', default=1, required=True,oldname='importe_tipo_metodo', help="Importe 01")
    
    #campo01 = fields.Char(string ='campo01', default='t', required = True)
    #payment_method_pb02 = fields.Many2one('pos.payment.method', string='Payment Method', required=True)
    
    #valor = fields.Float(string='valor', compute='_get_last', store=True)
    
    
    #@api.depends('importe_tipo_metodo')
    #def _get_last(self):
    #    reg =[]
        
    #    for rec in self:
    #        reg.append(rec.importe_tipo_metodo)
    #    suma = sum([x.importe_tipo_metodo for x in reg])
    #    raise ValidationError(suma)
        
            
            
    #@api.constrains('importe_tipo_metodo')
    #def _check(self):
    #    for record in self:
    #        if self.importe_tipo_metodo > 0.00:
    #            raise ValidationError(record.importe_tipo_metodo)
            
    
    
    
    
    
    
    
    
