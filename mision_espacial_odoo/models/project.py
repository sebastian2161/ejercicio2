# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MisionProyecto(models.Model):
    _inherit = 'project.project'
    
    mision_id = fields.Many2one(comodel_name='mision.mision_espacial',
                                string='Proyecto Mision')
    
    
    
    
    #compilacion
    