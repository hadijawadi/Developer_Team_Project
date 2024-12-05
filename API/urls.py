
from django.urls import path
from first_app.views import send_saled_products

urlpatterns =[
    path('saled_products/',send_saled_products)

]