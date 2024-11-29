from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import Products
from.models import UserCart,CartItem
from django.http  import HttpResponse
from .models import UserCart

@login_required
def show_user_cart(request):
    user= request.user
    # user = UserCart.objects.get(user= username)
    # print(user)
    cart_items = UserCart.objects.filter(user=user)
    context = {
        'products':cart_items
    }
 
   
    return render(request,'user_cart_app/pages/user_cart.htm',context)





@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_slug = request.POST.get('slug')
        print(product_slug)
        product = get_object_or_404(Products, slug=product_slug)
        if not product_slug:
            return HttpResponse("Product slug is missing.")
        quantity = request.POST.get('quantity')
        user_product = UserCart.objects.create(
            user=request.user,
            product_name = product,
            product_amount = quantity,

        )
        user_product.save()
        return redirect('user_cart_app:show_user_cart')



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

