from django.urls import  path

from user_app.views import logout_view
from .views import *

urlpatterns = [
    path("", product_list_view, name='product-list'),
    path('detail/<uuid>/<slug>/', product_detail_view , name='product-detail'),
    path('category/<int:id>/', category, name="category"),
    path("log-out/", logout_view, name="log-out")
]