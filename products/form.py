from pyexpat import model
from django import forms
from products.models import ProductModel,MessageModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields =     ['product_name','product_price','product_details','product_image','product_category','product_description']

class UpdateForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields =     ['product_name','product_price','product_details','product_description']



class MessageForm(forms.ModelForm):
    class Meta:
        model=MessageModel
        fields ="__all__"