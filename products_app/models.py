from django.db import models
from django.utils.text import slugify


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
    product_discount = models.CharField(max_length=100,null=True,blank=True)
    product_is_new = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # for showing in the details page 
    slug = models.SlugField(blank=True,unique=True)

    def save(self, *args, **kwargs):
        # Generate unique slug for each product in order to avoid bugs 
        original_slug = slugify(self.product_name)
        unique_slug = original_slug
        num = 1
        while Products.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{original_slug}-{num}"
            num += 1
        
        self.slug = unique_slug
        super().save(*args, **kwargs)
    

    def __str__(self) -> str:
        return self.product_name
    
