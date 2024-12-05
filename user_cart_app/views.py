from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import Products,SpecialProducts
from saled_products.models import SaledProducts
from.models import UserCart,CartItem
from django.http  import HttpResponse
from .models import UserCart
from django.db import transaction


@login_required(login_url='account_app:register_user')
def show_user_cart(request):
    user= request.user
    # user = UserCart.objects.get(user= username)
    # print(user)
    cart_items = UserCart.objects.filter(user=user)
    for x in cart_items:
        print(x)
    print(cart_items)
    context = {
        'products':cart_items
    }
 

    return render(request,'user_cart_app/pages/user_cart.htm',context)


@login_required(login_url='account_app:register_user')
def add_to_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_price= request.POST.get('product_price')
        product_amount = request.POST.get('product_amount')
        print('this is product name <<<<<?????',product_name,product_price,product_amount)
        UserCart.objects.create(
            user = request.user,
            product_name = product_name,
            product_price = product_price,
            product_amount= product_amount,
        )
        return redirect('user_cart_app:show_user_cart')

# def add_to_cart(request):
#     if request.method == 'POST':
#         user= request.user
#         product_name = request.POST.get('product_name')
#         product_price = request.POST.get('product_price')
#         print(product_price)
#         product_amount = request.POST.get('product_amount')
#         new_cart = UserCart.objects.create(user= user,product_name = product_name, product_amount = product_amount,product_price = product_price)
#         new_cart.save()
#         return redirect('user_cart_app:show_user_cart')
#     return redirect('user_cart_app:show_user_cart')


# def add_to_cart(request):
#     if request.method == 'POST':
#         product_slug = request.POST.get('slug')
#         quantity = request.POST.get('product_amount')
        
#         product = get_object_or_404(Products, slug=product_slug)
        
#         user_product = UserCart.objects.create(
#             user=request.user,
#             product_name = product.product_name,
#             product_amount = quantity,
#             product_price = product.product_price,
#             # slug = product_slug

#         )
#         user_product.save()
#         return redirect('user_cart_app:show_user_cart')
#     return redirect('user_cart_app:show_user_cart')


# for adding from  special products  to user cart 
# @login_required(login_url='account_app:register_user')
# def add_to_cart_spcial(request):

#     if request.method == 'POST':
#         product_slug = request.POST.get('slug')
#         print(product_slug)
#         quantity = request.POST.get('quantity')
        

#         product= get_object_or_404(SpecialProducts, slug=product_slug)
#         if not product_slug:
#             return HttpResponse("Product slug is missing.")
        
#         user_product = UserCart.objects.create(
#             user=request.user,
#             product_name_special= product,
#             product_amount = quantity,
#             product_price = product.product_price,
#             slug= product_slug,

#         )
#         user_product.save()
#         return redirect('user_cart_app:show_user_cart')
#     return redirect('user_cart_app:show_user_cart')


# user wants to buy for handling from noraml products hadi javadi 
@login_required(login_url='account_app:register_user')
def buy(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_id = request.POST.get('product_id')
        print('product_id is :',product_id)
        product_price = request.POST.get('product_price')
        product_amount = request.POST.get('product_amount')
        SaledProducts.objects.create(
            customer = request.user,
            product_name=product_name,
            product_price=product_price,
            product_amount=product_amount
        )
        context = {
            'product_name':product_name,
            'product_price':product_price,
            'product_amount':product_amount,
        }
        return render(request,'user_cart_app/pages/after_buy.htm',context)
    # it shoudl return un to a page and should show detail if time 

# def buy(request):
#     if request.method == 'POST':
#         id = request.POST.get('id')

#         try:
#             with transaction.atomic():
#                 # Fetch the UserCart item using the slug
#                 product = get_object_or_404(UserCart, slug=id)
#                 print(product)

#                 # Determine product details for reference (optional)
#                 # if product.product_name_special:
#                 #     product_details = product.product_name_special
#                 # elif product.product_name:
#                 #     product_details = product.product_name
#                 # else:
#                 #     return HttpResponse("Invalid product configuration.")

#                 # Create a new sale in SaledProducts
#                 new_sale = SaledProducts.objects.create(
#                     customer=request.user,
#                     product_name=product,  # Pass the UserCart instance
#                     product_price=product.product_price,  # Use UserCart's price
#                     product_amount=product.product_amount  # Use UserCart's amount
#                 )
#                 print(f"SaledProducts created without atomic transaction: {new_sale}")


#                 # Delete the item from UserCart
#                 product.delete()

#                 return HttpResponse('Your purchase was successful')

#         except Exception as e:
#             return HttpResponse(f'An error occurred: {str(e)}')

#     return redirect('user_cart_app:show_user_cart')





# for deleting a product from cart page 
def delete_product(request,id):
    product = get_object_or_404(UserCart, id=id)
    product.delete()
    return redirect('user_cart_app:show_user_cart')



    
   

