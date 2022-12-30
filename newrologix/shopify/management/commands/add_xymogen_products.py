from api_endpoint.models import XymogenApi, ShopifyApi
from django.core.management.base import BaseCommand
from requests.auth import HTTPBasicAuth
import requests, json


def product_exists(product):
    pass


class Command(BaseCommand):
    def handle(self, *args, **options):
        xymogen_apis = XymogenApi.objects.all()
        if xymogen_apis.count():
            xymogen_api = xymogen_apis[0]
        else:
            raise Exception("No Xymogen API found.")
        shopify_apis = ShopifyApi.objects.filter(environment='dev')
        if shopify_apis.count():
            shopify_api = shopify_apis[0]
        else:
            raise Exception("No Shopify API found.")

        xheaders = {'username':xymogen_api.username,
                    'password':xymogen_api.password}
        xurl = xymogen_api.base_url + "ProductList"
        xreq = requests.get(xurl,
            auth=HTTPBasicAuth(xymogen_api.username,
                               xymogen_api.password))
        xproducts = xreq.json()
        for xproduct in xproducts:


            """curl -X GET "https://your-development-store.myshopify.com/admin/api/2022-10/products.json" \
    -H "X-Shopify-Access-Token: {access_token}"""
            sheaders = {'X-Shopify-Access-Token':shopify_api.access_token,
                        'Content-Type': 'application/json'}
            surl = shopify_api.base_url + "products.json"
            print(surl)
            drs = xproduct.get('drs', None)
            if drs:
                drs = drs.strip()
            body_html = xproduct['descriptionFull']
            if drs:
                body_html = "<a href='{}' target=_blank>Doctor Reference Sheet</a><p>&nbsp;</p>{}".format(drs, body_html)
            params = {"product":{"title":xproduct['productName'],
                                 "body_html": body_html,
                                 "vendor":xproduct['brand'].replace("XYMOGEN", "NEWROLOGIX"),
                                 "product_type":xproduct['countUnit'],
                                 "tags":xproduct['categories'].split(","),
                                 "images":[{"src":xproduct['productImage']}],
                                 "variants": [
                                     {
                                         "option1": xproduct['productName'],
                                         "price": xproduct['wholesalePrice'],
                                         "sku": xproduct['sku'],
                                         "barcode": xproduct['upc'],
                                         "inventory_quantity":xproduct['quantity'],
                                     }
                                 ]
                                 }}
            sreq = requests.post(surl, headers=sheaders, json=params)
            print(sreq.status_code)
            if sreq.status_code != 201:
                print(sreq.text)
                break
            else:
                print(json.dumps(sreq.json(), indent=2))
                # product = sreq.json()['product']
                # variant = product['variants'][0]
                # image_id = product['image']['id']
                # svariant = {}
                # id = variant['id']
                # svariant['variant'] = {}
                # svariant['id'] = id
                # svariant['option1'] = xproduct['weightUnit']
                # svariant['image_id'] = image_id
                # svariant['price'] = xproduct['wholesalePrice']
                # svariant['sku'] = xproduct['sku']
                # svariant['barcode'] = xproduct['upc']
                # svariant['weight'] = xproduct['weight']
                # svariant['weight_unit'] = xproduct['weightUnit']
                # vurl = shopify_api.base_url + "variants/{}.json".format(id)
                # print(vurl)
                # sreq = requests.put(vurl, json=svariant, headers=sheaders)
                # if sreq.status_code != 201:
                #     print(sreq.text)
                # else:
                #     print(json.dumps(sreq.json(), indent=2))
