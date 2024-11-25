from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import Products
from.models import UserCart,CartItem

def show_user_cart(request):
    if request.user.is_authenticated:
        return render(request,'user_cart_app/pages/user_cart.htm')

    return render(request,'user_cart_app/pages/user_cart.htm')


@login_required
def add_to_cart(request, slug):
    # Get the product or return a 404 error if not found
    product = get_object_or_404(Products, slug=slug)
    
    # Try to get the user's cart, create if it doesn't exist
    cart, created = UserCart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart, 
        product=product,
        defaults={'quantity': 1}
    )
    
    # If the item already exists, increase the quantity
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Redirect to cart or wherever you want
    return redirect('view_cart')  # Assume you have a named URL for cart view

# @login_required
# def update_cart_item(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    
#     if request.method == 'POST':
#         quantity = request.POST.get('quantity')
#         try:
#             quantity = int(quantity)
#             if quantity > 0:
#                 cart_item.quantity = quantity
#                 cart_item.save()
#             else:
#                 # Remove item if quantity is 0
#                 cart_item.delete()
#         except ValueError:
#             # Handle invalid quantity input
#             pass
    
#     return redirect('view_cart')

# @login_required
# def remove_from_cart(request, cart_item_id):
#     cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
#     cart_item.delete()
#     return redirect('view_cart')

