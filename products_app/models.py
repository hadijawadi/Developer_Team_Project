from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=250)
    product_price = models.IntegerField()
    product_description = models.TextField(null=True,blank=True,max_length=500)
    product_first_image = models.ImageField(upload_to='products/Images',)
    product_second_image = models.ImageField(upload_to='products/Images',)
    product_third_image = models.ImageField(upload_to='products/Images',null=True,blank=True)
    prodcut_fourth_image = models.ImageField(upload_to='products/Images',null=True,blank=True)
    # category = models.CharField(max_length=250)
    # sub_category = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

    def __str__(self) -> str:
        return self.product_name
    
