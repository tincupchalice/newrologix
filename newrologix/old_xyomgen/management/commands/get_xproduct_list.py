from ...models import XyomgenProduct, Flavor, UnitCount, Brand, Category, XProductCategoryMap
from django.core.management.base import BaseCommand
from requests.auth import HTTPBasicAuth
import requests, json

na = "N/A"

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
        ret = requests.post(api_call, headers=url_headers, params=data)
    else:
        ret = requests.post(api_call, headers=url_headers)

    if ret.status_code == 200:
        js = ret.json()
        return js
    else:
        raise Exception("{}->{}".format(ret.status_code, ret.text))


def get_product_list():
    context = {'headers': url_headers}
    return get_api_call(api_product_list_url)


class Command(BaseCommand):
    def handle(self, *args, **options):
        js = get_product_list()
        for record in js:
            categories = []
            brands = []
            unit_counts = []
            flavors = []
