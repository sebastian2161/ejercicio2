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
        return http.request.render('odoo_academy.hello')
    