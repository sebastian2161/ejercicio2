# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectWizard(models.TransientModel):
    
    _name = 'mision.project.wizard'
    _description = 'Wizard: Rapido creación de un projecto en el modulo de mision-Lanzamiento'
    
    def _default_mision(self):
        return self.env['mision.mision_espacial'].browse(self._context.get('active_id'))
    
    
    mision_id = fields.Many2one(comodel_name='mision.mision_espacial',
                                string='Mision',
                                required=True,
                                default= _default_mision)
    
    
    projecto = fields.Char(string ='Project', required = True)
    email = fields.Char(string ='Email', required = True)
    
    
    def create_project(self):
        project_id = self.env['project.project'].create({
            'name': self.projecto,
            'alias_name': self.email,
            'mision_id' : self.mision_id.id
            
            })
            
    
    
    