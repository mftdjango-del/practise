from django.urls import path
from .views import *


urlpatterns = [
    path("blog-list/", BlogListView.as_view(), name='blog-list'),
    path("blog-detail/<slug:slug>/", BlogDetailView.as_view(), name='blog-detail')
]