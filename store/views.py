from django.shortcuts import render, redirect
from .models import Product, Category

def product_list(request):
    products = Product.objects.filter(avaliable=True)
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, 'store/product_list.html', context)

def product_details(request, category_slug):
    products = Product.objects.filter(categories__slug=category_slug)
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, 'store/product_list.html', context)