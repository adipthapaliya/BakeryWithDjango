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
from products import views
urlpatterns = [
    path('admin/addproduct',views.add_product),
        path('admin/updateproduct/<int:id>',views.update_product),

    path('admin/delete/<int:id>',views.delete_product),
    path('user/sendmessage',views.add_message),
    path('admin/edit/<int:id>',views.edit),
    path('admin/delete/<int:id>',views.delete),
    path('admin/special/<int:id>',views.special),
        path('admin/removespecial/<int:id>',views.remove_special),

    path('buynow/<int:id>/<int:uid>',views.buy_product),
        path('buy_delete/<int:id>/<int:uid>',views.delete_buy),



    


        
    



    
]