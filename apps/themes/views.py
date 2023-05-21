from django.shortcuts import get_object_or_404, render
from apps.themes.models import ParentTheme, ChildTheme
from apps.products.models import Product
from apps.products.forms import ProductSearchForm, ProductSortForm


def all_themes_index(request):

    parent_theme = ParentTheme.objects.filter(is_active=True)
    child_theme = ChildTheme.objects.filter(is_active=True)

    return render(request, 'base/index.html', 
                  {'parent_theme': parent_theme, 'child_theme': child_theme})

def all_themes(request):

    parent_theme = ParentTheme.objects.filter(is_active=True)
    child_theme = ChildTheme.objects.filter(is_active=True)

    return render(request, 'themes/all_themes.html', 
                  {'parent_theme': parent_theme, 'child_theme': child_theme})


def theme_posts(request, slug):
    child_theme = get_object_or_404(ChildTheme, slug=slug)
    products = Product.objects.filter(child_theme=child_theme)

    search_form = ProductSearchForm(request.GET)
    sort_form = ProductSortForm(request.GET)

    
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

    return render(request, 'themes/theme_post.html', {'child_theme': child_theme, 'products': products, 
                                                      'search_form': search_form, 'sort_form': sort_form})

