from django.http import HttpResponse, JsonResponse
from django.template import loader
from requests.auth import HTTPBasicAuth
import requests, json
from collections import OrderedDict
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


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
           'productImage', 'drs', 'categories', 'quantity', 'count',
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
        ret = requests.post(api_call, headers=url_headers, params=data)
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


@login_required(login_url='/accounts/login/')
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
    for i, record in enumerate(js):
        elt = OrderedDict()
        for header in headers:
            if i < 5: print(header, record.get(header, "N/A"), type(record.get(header, "N/A")))
            elt[header] = record.get(header, "")
        data.append(elt)
    context['data'] = data
    template = loader.get_template('xyomgen/product_list.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def create_order(request):
    # form to create order
    context = {}
    template = loader.get_template('xyomgen/create_order.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def order_created(request):
    post = request.POST
    if post:
        # add form values
        pass
    else:
        # revert to form with partial values
        pass
    context = {}
    template = loader.get_template('xyomgen/order_accepted.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def order_status(request):
    pass


@login_required(login_url='/accounts/login/')
def cancel_order(request):
    pass


@login_required(login_url='/accounts/login/')
def order_canceled(request):
    pass

### THIS IS FOR CLIENT SIDE LATER
# @login_required(login_url="/users/login")
# def cart_add(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("home")
#
#
# @login_required(login_url="/users/login")
# def item_clear(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.remove(product)
#     return redirect("cart_detail")
#
#
# @login_required(login_url="/users/login")
# def item_increment(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.add(product=product)
#     return redirect("cart_detail")
#
#
# @login_required(login_url="/users/login")
# def item_decrement(request, id):
#     cart = Cart(request)
#     product = Product.objects.get(id=id)
#     cart.decrement(product=product)
#     return redirect("cart_detail")
#
#
# @login_required(login_url="/users/login")
# def cart_clear(request):
#     cart = Cart(request)
#     cart.clear()
#     return redirect("cart_detail")
#
#
# @login_required(login_url="/users/login")
# def cart_detail(request):
#     return render(request, 'cart/cart_detail.html')