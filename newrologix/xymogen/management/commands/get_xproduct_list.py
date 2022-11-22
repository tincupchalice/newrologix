from ...models import XymogenProduct, Flavor, UnitCount, Brand, Category, XProductCategoryMap, XProductDefaultDosingMap
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
            cat = record['categories']
            newcats = []
            newcat = Category()
            if cat:
                cats = cat.split(",")
                for c in cats:
                    categories = Category.objects.filter(category_name=c)
                    if not categories.count():
                        newcat.category_name = c
                        try:
                            newcat.clean()
                            newcat.save()
                            newcats.append(newcat)
                        except Exception as e:
                            print(str(e))
                    else:
                        newcats.append(categories[0])
            brand = record['brand']
            if not brand: brand = "N/A"
            b = Brand()
            if brand:
                brands = Brand.objects.filter(brand_name=brand)
                if not brands.count():
                    b.brand_name = brand
                    try:
                        b.clean()
                        b.save()
                    except Exception as e:
                        print(str(e))
                else:
                    b = brands[0]
            unit_count = record['countUnit']
            if not unit_count: unit_count = "N/A"
            ucount = UnitCount()
            if unit_count:
                unit_counts = UnitCount.objects.filter(unit_count_name=unit_count)
                if not unit_counts.count():
                    ucount.unit_count_name = unit_count
                    try:
                        ucount.clean()
                        ucount.save()
                    except Exception as e:
                        print(str(e))
                else:
                    ucount = unit_counts[0]
            flavor = record['flavor']
            if not flavor: flavor = "N/A"
            f = Flavor()
            if flavor:
                flavors = Flavor.objects.filter(flavor_name=flavor)
                if not flavors.count():
                    f.flavor_name = flavor
                    try:
                        f.clean()
                        f.save()
                    except Exception as e:
                        print(str(e))
                else:
                    f = flavors[0]
            products = XymogenProduct.objects.filter(productName=record['productName']).filter(upc=record['upc'])
            if not products.count():
                product = XymogenProduct()
                product.productName = record['productName']
                product.sku = record['sku']
                product.quantity = record['quantity']
                product.releaseDate = record['releaseDate']
                product.wholesalePrice = record['wholesalePrice']
                product.retailPrice = record['retailPrice']
                product.upc = record['upc']
                product.flavor = f
                product.brand = b
                product.descriptionShort = record['descriptionShort']
                product.supplementFactsHTML = record.get('supplementalFactsHTML', "N/A")
                product.drs = record['drs']
                product.unitCount = ucount
                product.unitWeight = record['weightUnit']
                product.weight = record['weight']
                product.productImage = record['productImage']
                try:
                    product.clean()
                    product.save()
                except Exception as e:
                    print(record['productName'], "Product:"+str(e))

                for newcat in newcats:
                    category_map = XProductCategoryMap()
                    category_map.product = product
                    category_map.category = newcat
                    try:
                        category_map.clean()
                        category_map.save()
                    except Exception as e:
                        print("CategoryMap"+str(e))

                dosings = record['defaultDosing']
                for dosing in dosings:
                    time = dosing['time']
                    qty = dosing['qty']
                    dose_map = XProductDefaultDosingMap()
                    dose_map.product = product
                    dose_map.time = time
                    dose_map.qty = qty
                    try:
                        dose_map.clean()
                        dose_map.save()
                    except Exception as e:
                        print("DoseMap"+str(e))




