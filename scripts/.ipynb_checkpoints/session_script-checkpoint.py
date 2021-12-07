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
                                'academy.session', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)


courses = models.execute_kw(db, uid, password,
                           'academy.course', 'search_read',
                           [[['base_price', '>', 50]]])
print(courses[1])


course = models.execute_kw(db, uid, password,
                          'academy.course', 'search',
                          [[['name', 'in',['ERP_101','ERP_acounting']]]])

print(course)

session_fields = models.execute_kw(db, uid, password,
                                  'academy.session', 'fields_get',
                                  [], {'attributes': ['string', 'type', 'required']})
#print(session_fields)


#new_session = models.execute_kw(db, uid, password,
#                            'academy.session', 'create',
#                            [
#                                {
#                                    'course_id': course[0],
#                                    'duration': 1,
#                                }
#                            ]
#                            )

#print(new_session)


update_rec = models.execute_kw(db, uid, password, 
                               'academy.session', 'write', 
                               [[course[0]], {'duration': 1}])

print(update_rec)