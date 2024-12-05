from django.shortcuts import render,redirect
from products_app.models import Products,SpecialProducts,Catagory
from rest_framework.decorators import api_view
from rest_framework.response import Response
from saled_products.models import SaledProducts
from first_app.sarilizers import SaledProductsSerilizers

# sending data to api 
@api_view(['GET'])
def send_saled_products(request):
    if request.method == 'GET':
        data = SaledProducts.objects.all()
        serilizer = SaledProductsSerilizers(data= data, many = True)
        return Response(serilizer.data)
    

#  here use this to bring the latest products 
# .order_by('-created_at') showing all products EXcept new products 
def home_view(request):
   
    products = Products.objects.filter(product_is_new= False)
    new_products = Products.objects.filter(product_is_new = True)
    context = {
        'products':products,
        'new_products':new_products,
    }
    return render(request,'index.html',context)



def new_products(request):
   
    products = Products.objects.filter(is_new = True)
    Special_products = SpecialProducts.objects.all().order_by('-created_at')
    for x in Special_products:
        print(x.product_name)
    context = {
        'products':products,
        'special_products':Special_products,
    }
    return render(request,'index.html',context)

# for searching among of products and catagories 
def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_input')  # Use .get() instead of ['']
        if search_query:  # Add a check to ensure search_query is not None
            products = Products.objects.filter(product_name__icontains=search_query)
            spe_products = SpecialProducts.objects.filter(product_name__icontains=search_query)
            catagory= Catagory.objects.filter(cata_name__icontains=search_query)
        #    search for catagory as well show catagoris to user as well .
            context = {
                'products': products,
                'spe_products': spe_products,
                'catagory': catagory,
                'search_query': search_query
            }
            return render(request, 'search_results.htm', context)
        return redirect('/')

    
