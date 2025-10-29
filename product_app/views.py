from django.http import Http404
from django.shortcuts import render, redirect
from .models import ProductModel, Category, Color


# Create your views here.
def product_list_view(request):
    products = ProductModel.objects.all()
    return render(request, "product-list-page.html", {
        'products': products
    })


def product_detail_view(request, uuid, slug):
    try:
        product = ProductModel.objects.get(uuid=uuid)
        colors = Color.objects.filter(colors=product)
    except:
        raise Http404

    return render(request, "product-detail-page.html", {
        "product": product,
        "colors": colors
    })
    
def category(request, id):
    category = Category.objects.filter(id=id).first()
    if not category:
        raise Http404
    products = ProductModel.objects.filter(category=category)
    return render(request, "product-list-page.html", {
        'products': products
    })



def test_function(request):
    pass