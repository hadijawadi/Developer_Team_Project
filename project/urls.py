
from django.contrib import admin
from django.urls import path,include
from first_app.views import home_view,search
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name='home_view'),
    path('search/', search,name='search_view'),
    path('product/',include('products_app.urls')),
    path('user_cart/',include('user_cart_app.urls')),
    path('catagory/',include('catagory_app.urls')),
    path('account/',include('account_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
