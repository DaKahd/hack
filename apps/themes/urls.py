from apps.themes import views
from django.urls import path, include


urlpatterns = [
    path('', views.all_themes),
    
]

