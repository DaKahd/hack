from apps.themes import views
from django.urls import path


urlpatterns = [
    path('', views.all_themes_index),
    path('chatbot', views.chatbot, name="chatbot"),
    path('shop-by-category/', views.all_themes, name='all_themes'),
    path('shop-by-category/<slug:slug>/', views.theme_posts, name='theme_posts')
    
]

