from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.


def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    
    paginator = Paginator(products, 7)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'products/category.html', {'category': category, 'prods': products})


def product_detail(request, category_id, product_id):
    product = get_object_or_404(
        Product, category_id=category_id, id=product_id)
    return render(request, 'products/product.html', {'product': product})


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_new.html'
    fields = ['title', 'category', 'price', 'stock',
              'image', 'description', 'available']


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_edit.html'
    fields = ['price', 'stock', 'description', 'available']


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('home')
