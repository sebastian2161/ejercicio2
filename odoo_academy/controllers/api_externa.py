# -*- coding: utf-8 -*-

from odoo import http
#from odoo import http
#import xmlrpc, xmlrpc.client
from xmlrpc import client
import re
import requests
import werkzeug.urls
import json



class externa(http.Controller):
    @http.route('/restfulapi/api_externa', auth='none', website=True)
    def api_externa(self, **kw):
            #req = requests.get('https://jsonplaceholder.typicode.com/users')
            #req = requests.get('https://sebastian2161-ejercicio21-demo-web-3894096.dev.odoo.com/restfulapi/get-products')
            return "Hola Mundo"
            #return req
        #req.raise_for_status()
        #parents_dict = req.json()
        #return parents_dict