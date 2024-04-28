from django.shortcuts import render
from django.views.generic import ListView, DetailView

from product.filters import ProductFilter
from product.models import Product


class ProductListView(ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'


    def get_queryset(self):
        return Product.objects.filter(active='True')



def get_all_products_per_category(request, pk):
    products_per_category = Product.objects.filter(category_id=pk)
    return render(request, 'product/list_of_products.html', {'all_products': products_per_category})


class ProductDetailView(DetailView):
    template_name = 'product/details_product.html'
    model = Product