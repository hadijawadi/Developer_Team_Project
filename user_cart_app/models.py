from django.db import models
from django.contrib.auth.models import User
from products_app.models import Products

class UserCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.ForeignKey(Products,on_delete=models.CASCADE)
    product_amount = models.IntegerField(null=True,blank=True,default=1)
    product_price = models.IntegerField(null=True,blank=True,default=1)


    def __str__(self) -> str:
        return f"{self.user.username} - {self.product_name} x{self.product_amount}"


class CartItem(models.Model):
    cart = models.ForeignKey(UserCart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def total_price(self):
        return self.product.price * self.quantity