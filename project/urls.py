
from django.contrib import admin
from django.urls import path,include
from first_app.views import home_view,search
from django.conf import settings
from django.conf.urls.static import static

#  for resetting user password 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name='home_view'),
    path('search/', search,name='search_view'),
    path('product/',include('products_app.urls')),
    path('user_cart/',include('user_cart_app.urls')),
    path('catagory/',include('catagory_app.urls')),
    path('account/',include('account_app.urls')),
    path('api/',include('API.urls')),
    # all of the following urls are for restting user password 
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name= 'account_app/pages/reset_password.htm'),name='reset_password'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name= 'account_app/pages/password_reset_done.htm'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name= 'account_app/pages/password_reset_confirm.htm'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name= 'account_app/pages/password_reset_complete.htm'),name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
