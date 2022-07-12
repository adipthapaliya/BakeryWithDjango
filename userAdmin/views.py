from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log
from django.contrib.auth import logout
from django.contrib import messages

from products.models import MessageModel

# Create your views here.
@login_required(login_url='/admin/login')

def home_page(request):
    return render(request,'admin/index.html')

@login_required(login_url='/admin/login')

def menu_page(request):
    return render(request,'admin/menu.html')


@login_required(login_url='/admin/login')
def message_page(request):
    message = MessageModel.objects.all()
    return render(request,'admin/message.html',{'message':message})



def login_page(request):
    return render(request,'login_register/admin_login.html')

def login_admin(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']    
        
        user = authenticate(request,username=username, password=password)

        if user is not None:
            if user.is_superuser == 1:

                log(request,user)
                return redirect('/admin/home')

            else:
                messages.error(request,"Username and Password Don't Match, Please Try Again !")
                return redirect('/admin/login')        
        else:
            messages.error(request,"Username and Password Don't Match, Please Try Again !")
            return redirect('/admin/login')


    else:
        messages.error(request,"Something is worng with your form validation, Please Try Again !")

        return redirect('admin/login')


def log_out(request):
    logout(request)
    return redirect('/admin/login')