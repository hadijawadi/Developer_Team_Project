from django.urls import path
from .views import show_details,show_special_product_detail
from django.conf import settings
from django.conf.urls.static import static

app_name ='products_app'

urlpatterns  = [
    path('show_details/<slug:slug>',show_details,name='show_details'),
    path('show_special_details/<slug:slug>',show_special_product_detail,name='show_special_product_details'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

