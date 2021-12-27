# -*- coding: utf-8 -*-

from odoo import http
#from odoo import http
#import xmlrpc, xmlrpc.client
from xmlrpc import client
import re
import requests
import werkzeug.urls



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
    
    @http.route('/academy/api', auth= 'public', website=True)
    def index(self, **kw):   
        sales_orders = http.request.env['sale.order'].search([])
        output = "<h1>Sales Orders</h1><ul>"
        
        for sale in sales_orders:
            output += '<li>' + sale['name'] + '</li>'
        output += "</ul>"
        
        return output
    

    
    # End-Point que busca el id del usuario activo 
    @http.route('/restfulapi/login', auth='none', website=True)
    def login(self, **kw):
        #xmlrpclib = xmlrpc.client
        
        url = 'https://sebastian2161-ejercicio21-rama-v12-3748221.dev.odoo.com'
        db = 'sebastian2161-ejercicio21-rama-v12-3748221'
        username = 'admin'
        password = 'admin'
         
        common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        #print(common.version())
        try:
            uid = common.authenticate(db, username, password, {})
            return json.dumps({'user_id':uid})
        except:
            return json.dumps({'Error':'Invalid Request'})
        
    
    
    
    # End-Point que lista todos los productos con sus precios.
    @http.route('/restfulapi/get-products', auth='none', website=True)
    def get_products(self, **kw):
        #xmlrpclib = xmlrpc.client
        
        url = 'https://sebastian2161-ejercicio21-rama-v12-3873200.dev.odoo.com'
        db = 'sebastian2161-ejercicio21-rama-v12-3873200'
        username = 'admin'
        password = 'admin'
    
        models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        #print(common.version())
        #return 'Hola Mundo'
        
        try:
            uid = common.authenticate(db, username, password, {})
            res = models.execute_kw(db, uid, password, 'product.product', 'search_read',
                                    [[['id', 'in',[15,318,361]]]], 
                                    {'fields': ['id', 'price', 'price_extra', 'lst_price', 'default_code']})
            
            return json.dumps({'products':res})
        except:
            return json.dumps({'Error':'Invalid Request'})
        
        
        
        
    # End-Point que busca un producto en especifico.    
    @http.route('/restfulapi/product/<int:var>', auth='none', website=True)
    def product(self,var, **kw):
        #xmlrpclib = xmlrpc.client
        
        url = 'https://sebastian2161-ejercicio21-rama-v12-3748221.dev.odoo.com'
        db = 'sebastian2161-ejercicio21-rama-v12-3748221'
        username = 'admin'
        password = 'admin'
    
        models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
        common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        #print(common.version())
        #return 'Hola Mundo'
        
        try:
            uid = common.authenticate(db, username, password, {})
            res = models.execute_kw(db, uid, password, 'product.product', 'search_read',
                                    [[['id', '=', int(var)]]], 
                                    {'fields': ['id', 'price', 'price_extra', 'lst_price', 'default_code']})
            
            return json.dumps({'products':res})
        except:
            return json.dumps({'Error':'Invalid Request'})
        

class externa(http.Controller):
    @http.route('/restfulapi/api_externa', auth='none', website=False)
    def api_externa(self, **kw):
        
        req = requests.get('https://jsonplaceholder.typicode.com/users', params=0)
        return req.json()
        #req.raise_for_status()
        #parents_dict = req.json()
        #return parents_dict
        
        
        
        
    # End-Point crear un producto nuevo    
    #@http.route('/restfulapi/crear_product/<string:prod>', auth='none', website=True)
    #def crear_product(self, prod, **kw):
        #xmlrpclib = xmlrpc.client
        
    #    url = 'https://sebastian2161-ejercicio21-rama-v12-3748221.dev.odoo.com'
    #    db = 'sebastian2161-ejercicio21-rama-v12-3748221'
    #    username = 'admin'
    #    password = 'admin'
    
    #    models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))
    #    common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
        #print(common.version())
        #return 'Hola Mundo'
        
        #try:
    #    uid = common.authenticate(db, username, password, {})
        #id1 = models.execute_kw(db, uid, password, 'product.template', 'create', [{'name': prod,}])
    #    id2 = models.execute_kw(db, uid, password, 'product.product', 'create', [{'default_code': prod,'categ_id':8}])
        
        
    #    return json.dumps({'products.product':id2, 'mensaje': 'Registro creado'})
        #except:
        #    return json.dumps({'Error':'Invalid Request'})