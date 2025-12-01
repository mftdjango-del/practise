from django.shortcuts import render
from django.views import View


# Create your views here.


class BlogListView(View):
    def get(self, request):
        return render(request, 'blog-list-page.html', {

        })


class BlogDetailView(View):
    def get(self, request, slug):
        return render(request, 'blog-detail-page.html', {

        })
    def post(self, request):
        pass

