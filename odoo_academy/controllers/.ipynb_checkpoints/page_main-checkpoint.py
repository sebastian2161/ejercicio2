# -*- coding: utf-8 -*- 
from odoo import http 
from xmlrpc import client
import re
import requests
import werkzeug.urls
import json




 
class Todo1(http.Controller): 
     
    @http.route('/hellocms/<page>', auth='public', website=True)
    def hello (self, page, ** kwargs):
        return http.request.render(page)