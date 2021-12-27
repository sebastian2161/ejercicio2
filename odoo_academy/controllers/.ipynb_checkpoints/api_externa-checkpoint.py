# -*- coding: utf-8 -*-

from odoo import http
#from odoo import http
#import xmlrpc, xmlrpc.client
from xmlrpc import client
import re
import requests
import werkzeug.urls



class externa():
    @http.route('/restfulapi/api_externa', type='json', auth='none', website=False)
    def api_externa(self, **kw):
            req = requests.get('https://jsonplaceholder.typicode.com/users')
            return req.json()
        #req.raise_for_status()
        #parents_dict = req.json()
        #return parents_dict