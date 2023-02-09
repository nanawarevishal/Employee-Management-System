"""office_emp_project URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from .import views



urlpatterns = [

    path('',views.home,name='home'),
    path('manage_emp',views.manage_emp,name='manage_emp'),
    path('all_emp/',views.all_emp,name='all_emp'),
    path('add_emp/',views.add_emp,name='add_emp'),
    # path('remove_emp/',views.remove_emp,name='remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp,name='remove_emp'),
    path('search_emp/',views.search_emp,name='search_emp'),
    path('search/',views.search,name='search'),
    path('handlesignup',views.handlesignup,name='handlesignup'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact')
    

    
]
