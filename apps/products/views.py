from django.shortcuts import get_object_or_404, render
from apps.products.models import Product


def all_products(request):

    products = Product.objects.all()
    return render(request, 'products/all_products.html', {'products': products})


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})