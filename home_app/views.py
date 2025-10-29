from django.shortcuts import render
import requests
from product_app.models import ProductModel, Category
from utils.utils import group_list


def home_page(request):
    products = ProductModel.objects.all()
    product_list = group_list(products, 4)
    return render(request, 'home.html', {
        'product_list': product_list
    })


def header_component(request):
    try:
        # send_request = requests.get("http://api.navasan.tech/latest/?api_key=freetwq7fS3guAD4log5lhZIT7bZ9Bcn")
        # gold = send_request.json()["18ayar"]["value"]
        gold = 10570000
    except Exception as e:
        print(e)
        gold = 0
    categories = Category.objects.filter(is_active=True)
    return render(request, 'header.html', {
        "gold": gold,
        "categories": categories
    })
def footer_component(request):
    return render(request, 'footer.html', {

    })
