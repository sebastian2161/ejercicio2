import shopify
import json
import requests


APIKey = '8864d2b177d3755f68f108513ac42936'
APIPass = 'd009ccf4df6faae1c020f421e6586d28'
TOKEN = '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'
NAME = 'sebastiancoll25'

# info to start the session
shop_url  = NAME + '.myshopify.com'
api_version = '2022-04'
access_token = TOKEN

# Start the session
shopify.Session.setup(api_key=APIKey, secret=APIPass)
session = shopify.Session(shop_url, api_version, access_token)
shopify.ShopifyResource.activate_session(session)

# Get the Store ID
shop = shopify.Shop.current()

print(shop)

# Get the Products Id
products = shopify.Product.find()

print(products)