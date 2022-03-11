# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string ='titulo', required = True)
    descripcion = fields.Text(string = 'descripcion')
    
    base_price = fields.Float(string='Base Price', default=0.00)
    
    additional_fee = fields.Float(string='Aditional Fee', default =10.00)
    
    
    total_price = fields.Float(string='total Price', default=0.00, readonly=True)
    
    session_ids = fields.One2many(comodel_name='academy.session',
                                  inverse_name='course_id',
                                  string='Sessions')
    
    @api.onchange('base_price','additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('No puede ingresar nro. negativos para Base Price')
        
        self.total_price = self.base_price + self.additional_fee
    
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if self.additional_fee < 10.0:
                raise ValidationError('Additional fee debe ser mayor a 10.0')
                
            
        
    