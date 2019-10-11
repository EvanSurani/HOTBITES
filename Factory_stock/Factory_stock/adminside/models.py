from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class addproductcat(models.Model):
    product_name = models.CharField(max_length = 20)
    category = models.CharField(max_length = 20)
    
    class Meta:
        db_table = "add_product_cat"
