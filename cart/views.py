# cart/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Product
from .models import Cart, CartItem

@login_required
def cart_detail(request):
    """Display the current user’s cart."""
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    
    try:
        quantity = int(request.POST.get('quantity', 1))
    except ValueError:
        quantity = 1

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        # Option 1: Increment existing quantity:
        cart_item.quantity += quantity
        # Option 2: Replace with new quantity:
        # cart_item.quantity = quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    messages.success(request, f"{product.name} added to your cart.")
    return redirect('cart_detail')


@login_required
def remove_from_cart(request, item_id):
    """Remove a specific cart item from the user’s cart."""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f"{product_name} removed from your cart.")
    return redirect('cart_detail')
