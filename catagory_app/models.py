from django.db import models


class Catagory(models.Model):
    cata_name = models.CharField(max_length=500,unique=True)


    def __str__(self):
        return self.cata_name
    
    