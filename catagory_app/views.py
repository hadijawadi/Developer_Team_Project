from django.shortcuts import render
from .models import Catagory
from django.shortcuts import render, get_object_or_404



# just for showing the three catagories that we have SAMSUNG,IPHONE,and XIOAMI
def show_catagories(request):
    Catagories = Catagory.objects.all()
    
    
    context = {
        'catagories':Catagories
    }
    return render(request,'catagory_app/pages/catagories.htm',context)



#   category = get_object_or_404(Catagory, slug=category_slug)  # Assuming Catagory has a slug field
    # products = Products.objects.filter(product_catagory=category)

def show_catagory_products(request,id):
    # data = Products.objects.get(id = id )
    catagory=get_object_or_404(Catagory,id= id) 
    products = catagory.products_set.all()
    print(products)
    context ={
        'products':products,
        'catagory':catagory
    }
    

    return render(request,'catagory_app/pages/show_catagory.htm',context)

