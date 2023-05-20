from django.shortcuts import render
from apps.themes.models import ParentTheme, ChildTheme


def all_themes(request):

    parent_theme = ParentTheme.objects.filter(is_active=True)
    child_theme = ChildTheme.objects.filter(is_active=True)

    return render(request, 'themes/all_themes.html', 
                  {'parent_theme': parent_theme, 'child_theme': child_theme})