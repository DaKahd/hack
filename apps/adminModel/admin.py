from django.contrib import admin
from apps.themes.models import ParentTheme, ChildTheme


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