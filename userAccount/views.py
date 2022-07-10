from django.shortcuts import render

# Create your views here.


# Home Page Render

def home(request):
    return render(request,'user/index.html')