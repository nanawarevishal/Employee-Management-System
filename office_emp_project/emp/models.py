from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50,null=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50,null=False)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='emp/images',default="")
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    skills = models.TextField(max_length=100)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()


    def __str__(self):
        return self.first_name

