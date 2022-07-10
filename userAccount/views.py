from django.shortcuts import render

# Create your views here.


# Home Page Render

def home_page(request):
    return render(request,'user/index.html')

def contact_page(request):
    return render(request,'user/contact.html')