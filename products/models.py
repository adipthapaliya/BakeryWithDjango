from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.CharField(max_length=10)
    product_details = models.TextField(max_length=225)
    product_image = models.FileField(upload_to="static/image/product",blank=False)
    product_category = models.CharField(max_length=20)
    product_description = models.CharField(max_length=225,default="No Description Avilable")
    special  = models.TextField(max_length=10,default=None,blank=True,null=True)


    class Meta:
        db_table= 'product'

class MessageModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    email = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=10)
    message = models.TextField(max_length=225)

    class Meta:
        db_table= 'message'


class BuyModel (models.Model):
    id = models.AutoField(auto_created=True,primary_key=True)
    product= models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

