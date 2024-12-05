from django.db import models
from django.contrib.auth.models import User
from products_app.models import Products,SpecialProducts
from django.utils.text import slugify




class UserCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=1000,null=True,blank=True)
    # product_name_special = models.ForeignKey(SpecialProducts,on_delete=models.CASCADE,null=True)
    product_amount = models.IntegerField(null=True,blank=True,default=1)
    product_price = models.CharField(null=True,blank=True,max_length=550)

   


    def __str__(self) -> str:
        return f"{self.user.username}  x{self.product_amount}"


class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.product.product_price * self.quantity