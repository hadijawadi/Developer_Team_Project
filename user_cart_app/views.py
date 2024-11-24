from django.shortcuts import render


def show_user_cart(request):
    return render(request,'user_cart_app/pages/user_cart.htm')
