from django.db import models
from django.contrib.auth.models import User
from products_app.models import Products

# class  UserOrder (models.Model):
#     full_name = models.ForeignKey(User,on_delete=models.CASCADE)
#     product_name = models.ForeignKey(Products,on_delete=models.CASCADE)
#     address = models.CharField(max_length=1000,)
#     explaination  = models.TextField(max_length=1000,null=True,blank=True)
#     phone_number = models.IntegerField(max_length=10)


#     def __str__(self) -> str:
#         return self.address
    