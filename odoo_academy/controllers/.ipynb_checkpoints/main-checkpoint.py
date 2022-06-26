# -*- coding: utf-8 -*- 
from odoo import http 
from xmlrpc import client
import re
import requests
import werkzeug.urls
import json




 
class Todo(http.Controller): 
 
    @http.route('/helloworld', auth='public', website=True) 
    def hello(self, **kwargs):
        print("Execution Here.........................")
        
        return http.request.render('odoo_academy.hello')
    
    @http.route('/todo/add', auth='public', website=True) 
    def add(self, **kwargs):
        users = http.request.env['res.users'].search([])
        #output = "<h1>Users</h1><ul>"
        
        #for var in users:
        #    output += '<li>' + var['name'] + '</li>'
        #output += "</ul>"
        #return output
        return http.request.render('odoo_academy.add', {})
    