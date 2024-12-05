from django.db import models
from user_cart_app.models import UserCart
from django.contrib.auth.models import User


class SaledProducts(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    # product_name = models.ForeignKey(UserCart, on_delete=models.SET_NULL, null=True)
    # product_name = models.ForeignKey(UserCart, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=1000,null=True,blank=True)
    product_amount = models.IntegerField(max_length=250,null=True,blank=True)
    product_price = models.IntegerField(null=True,blank=True)


    def __str__(self) -> str:
        return self.customer.username

    