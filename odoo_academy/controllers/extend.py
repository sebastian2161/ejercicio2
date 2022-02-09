# -*- coding: utf-8 -*- 
from odoo import http 
from odoo.addons.odoo_academy.controllers.main import Todo
from xmlrpc import client
import re
import requests
import werkzeug.urls
import json
 
class TodoExtended(Todo): 
    @http.route('/hola/<string:name>')
    def hello(self, name=None, **kwargs): 
        response = super(TodoExtended, self).hello() 
        response.qcontext['name'] = name
        return response
        #return http.request.render('odoo_academy.hello_extended',{
        #    'name': name,
        #})