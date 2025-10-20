from django.urls import  path
from .views import *

urlpatterns = [
    path("", product_list_view, name='product-list'),
    path('detail/<uuid>/<slug>/', product_detail_view , name='product-detail')
]