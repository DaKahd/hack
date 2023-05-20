from apps.products import views
from django.urls import path


urlpatterns = [
    path('', views.all_products),
    path('<slug:slug>/', views.product_detail)
    
]

