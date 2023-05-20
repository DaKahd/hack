from apps.themes import views
from django.urls import path, include


urlpatterns = [
    path('', views.all_themes),
    path('shop-by-category/<slug:slug>', views.theme_posts)
    
]

