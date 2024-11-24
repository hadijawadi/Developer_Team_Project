from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Products


def show_details(request,slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'products_app/pages/show_detail.htm', {'product': product})


    