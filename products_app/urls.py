from django.urls import path
from .views import show_details
from django.conf import settings
from django.conf.urls.static import static

app_name ='products_app'

urlpatterns  = [
    path('show_details/<slug:slug>',show_details,name='show_details')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

