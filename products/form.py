from pyexpat import model
from django import forms
from products.models import ProductModel,MessageModel

class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields ="__all__"


class MessageForm(forms.ModelForm):
    class Meta:
        model=MessageModel
        fields ="__all__"