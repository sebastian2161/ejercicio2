# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Mision(models.Model):
    
    _name = 'mision.mision_espacial'
    _description = 'Mision Info'
    
    nave_espacial_id = fields.Many2one(comodel_name='mision.nave_espacial',
                                string='Nave',
                                ondelete='cascade',
                                required=True)
    
    name = fields.Char(string='Title', related='nave_espacial_id.name')
    
    fecha_lanza = fields.Datetime(string ='fecha_lanza')
    fecha_regreso = fields.Datetime(string ='fecha_regreso')
    
    tripulacion = fields.Many2many(comodel_name='res.partner', string='tripulacion')
    
    proyectos = fields.One2many(comodel_name='project.project',
                                inverse_name='mision_id',
                                string='proyectos')