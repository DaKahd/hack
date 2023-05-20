from django.shortcuts import get_object_or_404, render
from apps.themes.models import ParentTheme, ChildTheme
from apps.products.models import Product


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

    return render(request, 'themes/theme_post.html', {'child_theme': child_theme, 'products': products})

