from django.shortcuts import render
from products_app.models import Products


#  here use this to bring the latest products 
# .order_by('-created_at')
def home_view(request):

    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request,'index.html',context)

# for searching among of products and catagories 
def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_input')  # Use .get() instead of ['']
        if search_query:  # Add a check to ensure search_query is not None
            products = Products.objects.filter(product_name__icontains=search_query)
        #    search for catagory as well show catagoris to user as well .
            context = {
                'products': products,
                'search_query': search_query
            }
            return render(request, 'search_results.htm', context)
    
