from django.urls import path
from .views import show_catagories,show_catagory_products

app_name = 'catagory_app'

urlpatterns  =[
    path('',show_catagories,name = 'show_catagories'),
    path('show_catagories/<int:id>/',show_catagory_products,name = 'show_catagory_product'),

]