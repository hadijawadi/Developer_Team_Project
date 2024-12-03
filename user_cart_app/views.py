from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import Products,SpecialProducts
from.models import UserCart,CartItem
from django.http  import HttpResponse
from .models import UserCart

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
        product_slug = request.POST.get('slug')
        quantity = request.POST.get('quantity')
        
        product = get_object_or_404(Products, slug=product_slug)
        if not product_slug:
            return HttpResponse("Product slug is missing.")
        
        user_product = UserCart.objects.create(
            user=request.user,
            product_name = product,
            product_amount = quantity,
            product_price = product.product_price,
            slug = product_slug

        )
        user_product.save()
        return redirect('user_cart_app:show_user_cart')
    return redirect('user_cart_app:show_user_cart')


# for adding from  special products  to user cart 
@login_required(login_url='account_app:register_user')
def add_to_cart_spcial(request):
    if request.method == 'POST':
        product_slug = request.POST.get('slug')
        print(product_slug)
        quantity = request.POST.get('quantity')
        

        product= get_object_or_404(SpecialProducts, slug=product_slug)
        if not product_slug:
            return HttpResponse("Product slug is missing.")
        
        user_product = UserCart.objects.create(
            user=request.user,
            product_name_special= product,
            product_amount = quantity,
            product_price = product.product_price,
            slug= product_slug,

        )
        user_product.save()
        return redirect('user_cart_app:show_user_cart')
    return redirect('user_cart_app:show_user_cart')



# user wants to buy for handling from noraml products hadi javadi 

def buy(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        product = UserCart.objects.get(slug=id )
        product_root = SpecialProducts.objects.get(slug=id)
        if product_root:
            product_root.delete()
            return HttpResponse('your purchase was successful')
        else :
            main = Products.objects.get(slug= id)
            main.delete()
            return HttpResponse('asdasd')

    return redirect('user_cart_app:show_user_cart')



def delete_product(request,id):
    product = get_object_or_404(UserCart, id=id)
    product.delete()
    return redirect('user_cart_app:show_user_cart')

    
   

