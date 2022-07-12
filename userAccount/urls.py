"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from userAccount import views
urlpatterns = [
    path('',views.home_page),
    path('index',views.home_page),
    path('home',views.home_page),
    path('contact',views.contact_page),
    path('about',views.about_page),
    path('login',views.login_page),
    path('register',views.register_page),
    path('register/user',views.register_user),
    path('login/user',views.login_user),
    path('logout',views.log_out),

    





    
]