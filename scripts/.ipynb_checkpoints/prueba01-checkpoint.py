# -*- coding: utf-8 -*-

import requests
import json
import sys


def API_JSON():

    url = 'https://jsonplaceholder.typicode.com/users/'
        
        #data = {'params': {'users': 100}}
    data = {'params': 0}
    headers={'content-type':'application/json'}
    resultado = requests.get(url, params=0)
    res = json.loads(resultado.content)

    #values =[]
    #values.append(res)
    #print(values)
    #print(type(res))
    
    values = []
    for r in res:
        values.append({"id":r["id"],"name":r["name"]})

    print(values)
    

        
    #for r in res:
    #    values.append({"id":r["id"],"name":r["name"]})

    #print(values)

    #for x in values:
    #    print(x["id"])
        
API_JSON()