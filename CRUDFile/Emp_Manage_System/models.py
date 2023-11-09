from django.db import models

# Create your models here.

# creating department table where name set as primary key
class Department(models.Model):
    name = models.CharField(max_length=240,null=False)
    location = models.CharField(max_length=240)
    def __str__(self) -> str:
        return self.name   # it will use to display the name in department

# creating role table where name set as primary key
class Role(models.Model):
    name = models.CharField(max_length=120,null=False)
    def __str__(self) -> str:
        return self.name   # it will use to display the name in role

# creating main Employee table where we are connecting another two tables by Foreign key and also set the propety where we if we delete the data from the employee table then the data will also remove from the another table
class Employe(models.Model):
    first_name = models.CharField(max_length=200,null=False)
    last_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE) #here we are connecting the two models by ForeignKey where we will proceed like this attribute_name = models.Foreignkey(class_name, on_delete = mention the delete type)
    bonus = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField(default=0)
    def __str__(self) -> str:
        return "%s,%s,%s"%(self.first_name, self.last_name,self.phone)    # it will use to display the first_name, last_name, department in employee
    # what is the significance of the %s in the above code.