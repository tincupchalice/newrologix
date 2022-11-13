from django.http import HttpResponse, JsonResponse
from django.template import loader
from django import template
from requests.auth import HTTPBasicAuth
import requests, json
from collections import OrderedDict

# Create your views here.
api_username = '10290408'
api_password = 'hM6cO3jH9eM2pF4p'
api_base_url = 'https://testservices.wholescripts.com/api/Orders/'
api_product_list_url = api_base_url + 'ProductList'
api_order_submit_url = api_base_url + 'Submit'
api_order_status_url = api_base_url + 'Status'
api_order_number_status_url = api_order_status_url + '?ordernum={}'
api_order_cancel_url = api_base_url + 'Cancel'

url_headers = {'Username': api_username, 'Password': api_password}

"""
{'defaultDosing', 'quantity', 'categories', 'count', 'weightUnit', 
'releaseDate', 'flavor', 'productName', 'medPaxDetails', 'sku', 
'retailPrice', 'wholesalePrice', 'descriptionShort', 'warnings', 
'drs', 'countUnit', 'weight', 'upc', 'medPaxSku', 'supplementFactsHTML', 
'productImage', 'descriptionFull', 'brand'}
"""
headers = ['productName', 'brand', 'descriptionShort',
           'productImage', 'categories', 'quantity', 'count',
           'countUnit', 'weight', 'weightUnit', 'defaultDosing', 'flavor',
           'wholesalePrice', 'retailPrice',
           'releaseDate', 'upc', 'sku', 'medPaxSku', 'medPaxDetails',
           'supplementalFactsHTML', 'descriptionFull', 'warnings']


def get_api_call(api_call, data={}):
    print(api_call)
    url_data = url_headers
    print(json.dumps(url_data))
    if data:
        for k, v in data.items():
            url_data[k] = v
        ret = requests.get(api_call,
                           auth=HTTPBasicAuth(api_username, api_password),
                           params=data)
    else:
        ret = requests.get(api_call,
                           auth=HTTPBasicAuth(api_username, api_password))

    if ret.status_code == 200:
        js = ret.json()
        return js
    else:
        raise Exception("{}->{}".format(ret.status_code, ret.text))


def post_api_call(api_call, data={}):
    if data:
        ret = requests.post(api_call, headers=url_headers, data=data)
    else:
        ret = requests.post(api_call, headers=url_headers)

    if ret.status_code == 200:
        js = ret.json()
        return js
    else:
        raise Exception("{}->{}".format(ret.status_code, ret.text))


def index(request):
    context = {}
    template = loader.get_template('xyomgen/index.html')
    return HttpResponse(template.render(context, request))


def get_product_list(request):
    extra_data = None
    if request.GET:
        print(json.dumps(request.GET, indent=2))
        if 'product_search' in request.GET or \
                'instockonly' in request.GET:
            if 'product_search' in request.GET:
                extra_data = {'search': request.GET['product_search']}
            if 'instockonly' in request.GET:
                if not extra_data: extra_data = {}
                if request.GET['instockonly'] == 'on':
                    extra_data['instockonly'] = 'true'
                else:
                    extra_data['instockonly'] = 'false'
    context = {'headers': headers}
    if extra_data: context['search_criteria'] = extra_data
    if extra_data:
        js = get_api_call(api_product_list_url, data=extra_data)
    else:
        js = get_api_call(api_product_list_url)
    data = []
    for record in js:
        elt = OrderedDict()
        for header in headers:
            if header == 'releaseDate':
                print(record[header], type(record[header]))
            elt[header] = record.get(header, "")
        data.append(elt)
    context['data'] = data
    template = loader.get_template('xyomgen/product_list.html')
    return HttpResponse(template.render(context, request))
