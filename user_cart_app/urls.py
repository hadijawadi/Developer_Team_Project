from django.urls import path
from .views import show_user_cart
from django.conf import settings
from django.conf.urls.static import static

app_name ='products_app'

urlpatterns  = [
    path('show_user_cart',show_user_cart,name='user_cart')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

