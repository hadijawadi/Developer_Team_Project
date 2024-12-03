from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Products,SpecialProducts
from django.contrib.auth.decorators import login_required


def show_details(request,slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'products_app/pages/show_detail.htm', {'product': product})

# this view is for showing special products detial page 


def show_special_product_detail(request,slug):
    special_products = get_object_or_404(SpecialProducts, slug=slug)
    return render(request, 'products_app/pages/show_special_products.htm', {'product': special_products})
    
    