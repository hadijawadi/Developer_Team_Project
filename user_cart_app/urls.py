from django.urls import path
from .views import show_user_cart,add_to_cart,delete_product,add_to_cart_spcial,buy
from django.conf import settings
from django.conf.urls.static import static

app_name ='user_cart_app'

urlpatterns  = [
    path('show_user_cart',show_user_cart,name='show_user_cart'),
    path('add_to_cart/',add_to_cart,name='add_to_cart'),
    # for adding speical products to cart 
    path('add_to_cart_sp/',add_to_cart_spcial,name='add_to_cart_special'),
    path('delete<int:id>',delete_product,name='delete_product'),
    # for deleting and sbuying product
    path('buy',buy,name='buy_product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

