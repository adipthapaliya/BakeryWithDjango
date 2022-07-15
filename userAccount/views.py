from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import ProductModel

# Create your views here.


# Home Page Render

def home_page(request):
    return render(request,'user/index.html')

def contact_page(request):
    return render(request,'user/contact.html')

def about_page(request):
    return render(request,'user/about.html')

def gallary_page(request):
    return render(request,'user/galary.html')

def login_page(request):
    return render(request,'login_register/user_login.html')

def login_user(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request,username=username, password=password)

        if user is not None:
            if user.is_superuser == 0:

                log(request,user)
                return redirect('/home')

            else:
                messages.error(request,"Username and Password Don't Match, Please Try Again !")
                return redirect('/login')        
        else:
            messages.error(request,"Username and Password Don't Match, Please Try Again !")
            return redirect('/login')


    else:
        messages.error(request,"Something is worng with your form validation, Please Try Again !")

        return redirect('/login')

def register_page(request):
    return render(request,'login_register/user_register.html')

def register_user(request):

    if request.method == 'POST':

        if request.POST['password'] == request.POST['confirmpassword']:

            User.objects.create_user(
                first_name = request.POST['fullname'],
                username = request.POST['username'],
                password = request.POST['password'],
                email = request.POST['phonenumber'],
            )

            messages.success(request,"Sucessfully Created Your Account, Now Procude to Login !")

            return redirect('/login')

        
        else:
            messages.error(request,"Password Don't Match, Please Try Again !")
            return redirect('/register')

    else:
        messages.error(request,"Something is worng with your form validation, Please Try Again !")

        return redirect('/register')

def log_out(request):
    logout(request)
    return redirect('/home')


def menu_page(request):
    cake = ProductModel.objects.all().filter(product_category='cake')
    cookies = ProductModel.objects.all().filter(product_category="cookies")
    cupcake = ProductModel.objects.all().filter(product_category="cupcake")
    desert = ProductModel.objects.all().filter(product_category="desert")
    dounot = ProductModel.objects.all().filter(product_category="dounot")

    special = ProductModel.objects.all().filter(special=1) 
    return render(request,'user/menu.html',{'special':special,'cake':cake,'cookies':cookies,'cupcake':cupcake,'desert':desert,'dounot':dounot})

def details(request,id):
    data = ProductModel.objects.get(id=id)

    return render(request,'user/details.html',{'data':data})