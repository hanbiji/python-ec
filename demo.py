import zeep
import json

appToken = 'xxxxxx'
appKey = 'xxxxxx'
wsdl = 'http://47.52.107.98/default/svc/wsdl'
client = zeep.Client(wsdl=wsdl)
# element = client.get_element('ns0:callService')
# print(element)

print('仓库')
params = {}
data = client.service.callService(paramsJson = json.dumps(params), appToken = appToken, appKey = appKey, service = 'getWarehouse')
data = json.loads(data)
for v in data['data']:
	print(v)

print('发货方式')
data = client.service.callService(paramsJson = json.dumps(params), appToken = appToken, appKey = appKey, service = 'getShippingMethod')
data = json.loads(data)
for v in data['data']:
	print(v)

params = {
	"pageSize":100,
    "page":1,
	"product_sku":"",
	"product_sku_arr":[],
	"warehouse_code":"",
	"warehouse_code_arr":[]
}

# data = client.service.callService(paramsJson = json.dumps(params), appToken = appToken, appKey = appKey, service = 'getProductInventory')
# data = json.loads(data)
# for v in data['data']:
# 	print(v)

print('产品详情')
params = {
	"pageSize":100,
    "page":1,
	"product_sku":"RLH70076",
	"product_sku_arr":[],
	"warehouse_code":"",
	"warehouse_code_arr":[]
}
data = client.service.callService(paramsJson = json.dumps(params), appToken = appToken, appKey = appKey, service = 'getProductList')
data = json.loads(data)
for v in data['data']:
	print(v)


print('运费')
shipping_method = ['FEDEX_GROUND_LA', 'FEDEX_SMART_POST', 'GROUND_HOME_DELIVERY']
shipping_name = {'FEDEX_GROUND_LA': '联邦快递陆运-洛杉矶', 'FEDEX_SMART_POST': '联邦快递-USPS末端派送', 'GROUND_HOME_DELIVERY': '联邦快递-住宅派送-洛杉矶'}
for method in shipping_method:
	params = {
		"warehouse_code": "USLA01",
	    "country_code": "US",
	    'postcode': '12345',
	    "shipping_method": method,
	    "weight": 19.5,
	    'length': 55.00,
	    'width': 55.00,
	    'height': 47.00
	}
	data = client.service.callService(paramsJson = json.dumps(params), appToken = appToken, appKey = appKey, service = 'getCalculateFee')
	data = json.loads(data)
	print(shipping_name[method], data)
