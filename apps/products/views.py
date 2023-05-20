from django.shortcuts import get_object_or_404, render
from apps.products.models import Product
from apps.themes.models import ParentTheme, ChildTheme


def all_products(request):

    products = Product.objects.filter(is_active=True)
    
    return render(request, 'products/all_products.html', {'products': products})


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
    parent_theme = ParentTheme.objects.filter(is_active=True)
    child_theme = ChildTheme.objects.filter(is_active=True)

    return render(request, 'products/product_detail.html', {'product': product, 
                                        'parent_theme': parent_theme, 'child_theme': child_theme})