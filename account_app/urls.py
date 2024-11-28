from django.urls import path
from .views import register_user,create_profile,test_email

app_name = 'account_app'

urlpatterns = [
    path('register/',register_user,name='register_user'),
    path('profile/',create_profile,name='complete_user_profile'),
    path('email/',test_email),
]