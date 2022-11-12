from django.http import HttpResponse, JsonResponse
from django.template import loader
from django import template
from requests.auth import HTTPBasicAuth

import requests, json
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


def get_api_call(api_call, data={}):
    print(api_call)
    url_data = url_headers
    print(json.dumps(url_data))
    if data:
        for k,v in data.items():
            url_data[k] = v
        ret = requests.get(api_call,
                           auth=HTTPBasicAuth(api_username, api_password),
                           data=data)
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


def get_product_list(request):
    js = get_api_call(api_product_list_url)
    str_js = json.dumps(js, indent=2)
    # temporary html to see objects
    keys = set()
    for record in js:
        key_list = record.keys()
        for key in key_list:
            keys.add(key)
    keys = list(keys)
    html = "<table border=1><tr>"
    for key in keys:
        html += "<th>{}</th>".format(key)
    html += "</tr>"
    for record in js:
        html += "<tr>"
        for key in keys:
            val = record.get(key, "")
            if key == 'productImage':
                html += "<td><img height=200 src='{}'></img></td>".format(val)
            else:
                html += "<td>{}</td>".format(val)
        html += "</tr>"
    html += "</html>"
    print(str_js)
    print(len(js))
    return HttpResponse(html)

