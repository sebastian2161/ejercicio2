# -*- coding: utf-8 -*-

from odoo import http


class Academy(http.Controller):
    @http.route('/academy/', auth='public', website=True)
    def index(self, **kw):
        #return "Hello, world"
        return http.request.render('odoo_academy.prueba_web')
    
    @http.route('/academy/courses/<int:var>', auth='public', website=True)
    def courses(self, var, **kw):
        #courses = http.request.env['academy.course'].search([])
        courses = http.request.env['academy.course'].search([('id', '=', int(var))])
        return http.request.render('odoo_academy.course_website', {
            'courses': courses,
        })
    
    
     #   @http.route('/academy/courses1/<model('academy.course'):course>', auth='public', website=True)
     #def courses1(self, course, **kw):
     #   return self.course(course.id)
     #   })