from django.urls import path
from .views import show_user_cart,add_to_cart
from django.conf import settings
from django.conf.urls.static import static

app_name ='user_cart_app'

urlpatterns  = [
    path('show_user_cart',show_user_cart,name='show_user_cart'),
    path('add_to_cart/',add_to_cart,name='add_to_cart'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

