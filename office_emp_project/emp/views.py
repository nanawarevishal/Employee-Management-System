
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee,Department
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate



# Create your views here.

def home(request):
    return render(request,'home.html')

def manage_emp(request):
    return render(request,'manage_emp.html')

def about(request):
    
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    # print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):

    if request.method == "POST":
        print("post")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept= int(request.POST.get('dept'))
        salary= int(request.POST.get('salary'))
        bonus= int(request.POST.get('bonus'))
        role = int(request.POST.get('role'))
        phone= request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        new_emp = Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,role_id=role,bonus=bonus,phone=phone,hire_date=datetime.now())
        new_emp.save()
        messages.success(request,"Employee data saved succefully")
       
        return render(request,'add_emp.html')

        
    
    else:
        print("GEt")
        # return HttpResponse("Employee added Successfully")
        return render(request,'add_emp.html')

    return render(request,'add_emp.html')

def remove_emp(request,emp_id=0):

    # if request.method == "POST":

    #     id = request.POST.get('first_name')
    #     print(id)

    #     emps = Employee.objects.all()

    #     context = {'emps':emps}

    #     for emp in emps:
    #         if id == emp.first_name:
    #             empremove = Employee.objects.get(first_name = id)
    #             empremove.delete()
    #             messages.success(request,"Employee removed Successfully")

    # else:

    #      return render(request,'remove_emp.html')    


    
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(emp_id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse('Employee Deleted Successfully')

        except:
            return HttpResponse("Enter the valid Entry...!")
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request,'remove_emp.html',context)

def search_emp(request):

    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {'emps':emps}

        return render(request,'all_emp.html',context)

    elif request.method == "GET":
        return render(request,'search_emp.html')

    else:
        return HttpResponse("An error is Occured..!")


def search(request):
    data = request.GET['search']
    context={}

    if len(data) > 20 or data=='':
        messages.warning(request,"Employee data not found try another one...!")
        alldata = Employee.objects.none()
        
    else:
        first_name = Employee.objects.filter(first_name__icontains=data)
        last_name = Employee.objects.filter(last_name__icontains=data)
        # dept = Department.objects.filter(dept__icontains=data)

        alldata = first_name.union(last_name)

        context= {"emps":alldata,'data': data}

    return render(request,'search.html',context)

def handlesignup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name= request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        if not username.isalnum():
            messages.warning(request, " Username must be characters and numbers only")
            return redirect('/')

        if len(username) > 10 :
            messages.warning(request, " Username should must be 10 characters only")
            return redirect('/')

        if pass1 != pass2:
            messages.warning(request, " password didn't match")
            return redirect('/')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.fname = first_name
        myuser.lname = last_name
        myuser.save()
        messages.success(request,"Your login account created successfully...!")
        return redirect("/")

    else:
        messages.warning(request,"Error 404 ")


def loginuser(request):
    if request.method == 'POST':
        loginuser = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(request,username = loginuser,password = loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"You are login successfully.....!")
            return redirect("/")

    else:
        return HttpResponse("Error: 404")

    

def logoutuser(request):
    logout(request)
    messages.success(request,"You are successfully logout...! ")
    return redirect('/')
    
    
