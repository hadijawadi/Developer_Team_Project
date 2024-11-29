from django.urls import path
from .views import register_user,create_profile,logout_user,login_user

app_name = 'account_app'

urlpatterns = [
    path('register/',register_user,name='register_user'),
    path('profile/',create_profile,name='complete_user_profile'),
    path('logout/',logout_user,name='logout_user'),
    path('login/',login_user,name='login_user'),
]