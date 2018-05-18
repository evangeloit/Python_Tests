import json

# from urllib.request import urlopen

import urllib2

# with urllib2.urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()

req = urllib2.Request("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")
response = urllib2.urlopen(req)
source = response.read()

data = json.loads(source) # load string -->Python object

# print(data['list']['resources'])
# print(json.dumps(data, indent=2))

# print(len(data['list']['resources'])) # length of the data object, of ['list'] and within that list we access ['resour'] =188

# # ///// CREATE AN EMPTY DICTIONARY /////
#
# usd_rates = dict()
# #
# # #////// LOOP THROUGH //////
#
# for item in data['list']['resources']:
#     name = item['resource']['fields']
#     price = item['resource']['fields']
#     print(name,price)
#     # usd_rates[name] = price


# print(usd_rates['USD/INR'])
# #////////////////////////////////
# usd_rates = dict()

# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price
#
# print(50 * float(usd_rates['USD/INR']))
