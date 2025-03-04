from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category

def store(request):
    products = Product.objects.filter(avaliable=True)
    categories = Category.objects.all()
    context = {
        "products": products,
        "categories": categories,
    }
    return render(request, 'store/store.html', context)

# def product_details(request, category_slug):
#     products = Product.objects.filter(categories__slug=category_slug)
#     categories = Category.objects.all()
#     context = {
#         "products": products,
#         "categories": categories,
#     }
#     return render(request, 'store/product_details.html', context)

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_details.html', {'product': product})
