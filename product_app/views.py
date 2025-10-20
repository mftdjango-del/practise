from django.http import Http404
from django.shortcuts import render, redirect
from .models import ProductModel
# Create your views here.
def product_list_view(request):
    products = ProductModel.objects.all()
    return render(request, "product-list-page.html", {
        'products': products
    })


def product_detail_view(request, uuid, slug):
    try:
        product = ProductModel.objects.get(uuid=uuid)
    except:
        raise Http404

    return render(request, "product-detail-page.html", {
        "product": product
    })