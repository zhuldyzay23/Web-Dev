from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Product, Category

# Create your views here.

def products(request):
    prod = list(Product.objects.values())
    return JsonResponse(prod, safe=False)

def product_detail(request, product_id):
    prod = list(Product.objects.filter(id=product_id).values())
    return JsonResponse(prod, safe=False)

def show_categories(request):
    categories = list(Category.objects.values())
    return JsonResponse(categories, safe=False)

def show_category(request, category_id):
    category = list(Category.object.filter(id = category_id).values())
    return JsonResponse(category, safe=False)
