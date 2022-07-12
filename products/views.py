from django.shortcuts import redirect, render

from products.form import MessageForm, ProductForm
from django.contrib import messages

from products.models import ProductModel

# Create your views here.

def add_product(request):

    if request.method == 'POST' :

        data = ProductForm(request.POST, request.FILES)
        data.save()

    else:
        messages.error(request,"Uable to add Product , Please Try Again")
        return redirect('/admin/menu') 

def delete_product(request,id):
    data = ProductModel.objects.get(id=id)
    data.delete()
    return redirect('/admin/menu')  

def edit(request,id):
    data = ProductModel.objects.get(id=id)
    return render(request,"admin/menu.html",{"product":data})



def add_message(request):

    if request.method == 'POST' :

        data = MessageForm(request.POST)
        data.save()
        messages.success(request,"Message Sucessfully Send ! We will Reply You Soon")

        return redirect('/contact')

    else:
        messages.error(request,"Uable to add Product , Please Try Again")
        return redirect('/admin/menu') 



