from xmlrpc import client

url= 'https://sebastian2161-ejercicio2-rama-v12-3598634.dev.odoo.com'
db= 'sebastian2161-ejercicio2-rama-v12-3598634'
username= 'admin'
password= 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'mision.mision_espacial', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)


nave = models.execute_kw(db, uid, password,
                          'mision.nave_espacial', 'search',
                          [[['id', '>', -1]]])

print(nave)


mision_fields = models.execute_kw(db, uid, password,
                                  'mision.mision_espacial', 'fields_get',
                                  [], {'attributes': ['string', 'type', 'required']})

print(mision_fields)



for x in nave:
    new_nave_mision = models.execute_kw(db, uid, password,'mision.mision_espacial', 'create',[{'nave_espacial_id':x,                                                      'fecha_lanza':'2020-01-01','fecha_regreso':'2021-03-01'}])
                    
                                        
    

