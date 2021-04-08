from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('products', views.products),
    path('products/<int:product_id>', views.product_detail),
    path('categories', views.show_categories),
    path('category/<int:category_id>/', views.show_category),


]
