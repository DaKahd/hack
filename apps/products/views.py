from django.shortcuts import get_object_or_404, render
from apps.products.models import Product
from apps.products.forms import ProductSearchForm, ProductSortForm


def all_products(request):
    search_form = ProductSearchForm(request.GET)
    sort_form = ProductSortForm(request.GET)
    products = Product.objects.all()

    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        products = products.filter(title__icontains=search_query)

    if sort_form.is_valid():
        sort_option = sort_form.cleaned_data['sort_option']
        if sort_option == 'lowest':
            products = products.order_by('price')
        elif sort_option == 'highest':
            products = products.order_by('-price')
        elif sort_option == 'sale':
            products = products.filter(sale=True)


    return render(request, 'products/all_products.html', {'products': products, 'search_form': search_form, 'sort_form': sort_form})

def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})