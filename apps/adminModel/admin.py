from django.contrib import admin
from apps.themes.models import ParentTheme, ChildTheme
from apps.products.models import Product


class ParentThemeAdmin(admin.ModelAdmin):

    list_display = ('title', 'is_active',)
    list_filter = ('is_active',)
    fields = ('title', 'description', 'is_active',)

admin.site.register(ParentTheme, ParentThemeAdmin)


class ChildThemeAdmin(admin.ModelAdmin):

    list_display = ('title', 'is_active',)
    list_filter = ('is_active',)
    fields = ('parent_theme', 'title', 'description', 'is_active', 'slug',)

admin.site.register(ChildTheme, ChildThemeAdmin)


class ProductAdmin(admin.ModelAdmin):

    list_display = ('title', 'price', 'is_active',)
    list_filter = ('is_active', 'in_progress',)
    search_fields = ('title',)
    fields = ('child_theme', 'title', 'image', 'description', 
              'price', 'sale_price', 'quantity',
              'is_active', 'in_progress', 'slug',)

admin.site.register(Product, ProductAdmin)
    