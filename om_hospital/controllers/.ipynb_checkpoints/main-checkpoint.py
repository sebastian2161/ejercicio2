from odoo import http
#from odoo import http
#import xmlrpc, xmlrpc.client
from xmlrpc import client
import re
import requests
import werkzeug.urls
import json

CORS = '*'



class Hospital(http.Controller):

    @http.route('/patient_webform', auth='public', website=True)
    def patient_webform(self, **kw):
        #print("Execution Here.........................")
        #doctor_rec = request.env['hospital.doctor'].sudo().search([])
        #print("doctor_rec...", doctor_rec)
        return http.request.render('om_hospital.create_patient', {})
        #return "Hello, world"
    
    @http.route('/create/webpatient', auth="public", website=True)
    def create_webpatient(self, **kw):
        
        http.request.env['hospital.patient'].sudo().create(kw)
        return http.request.render("om_hospital.patient_thanks", {})
        
    
    
    