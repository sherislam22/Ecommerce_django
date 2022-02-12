
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Products, Category

from django.shortcuts import render

class ShopView(ListView):
    model = Products
    paginate_by = 6
    template_name = "shop.html"


# Create your views here.
class ProductViewList(ListView):
    model = Products
    template_name = 'category.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/detail.html'
    context_object_name = 'product'

class CategoListView(View):
    def get(self, *args, **kwargs):
        categories = Category.objects.all()
        return render(request, "category.html", {"categories": categories})

class CategoryView(View):
    def get(self, *args, **kwargs):
        category = Category.objects.get(slug=self.kwargs['slug'])
        item = Products.objects.filter(category=category)
        context = {
            'object_list': item,
            'category_title': category,
            
        }
        return render(self.request, "category.html", context)


