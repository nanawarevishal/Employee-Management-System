from django.contrib import admin
from .models import Employee,Role,Department
# Register your models here.

class MyEmp(admin.ModelAdmin):
    list_display = ('emp_id','first_name','last_name','dept','salary','bonus','role','phone','hire_date')


class MyRole(admin.ModelAdmin):
    list_display = ['name']


class MyDept(admin.ModelAdmin):
    list_display = ('name','location')




admin.site.register(Employee,MyEmp)
admin.site.register(Role,MyRole)
admin.site.register(Department,MyDept)