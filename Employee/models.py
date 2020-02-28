from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(unique=True,max_length=10)
    emp_fname = models.CharField(max_length=20,default="")
    emp_lname = models.CharField(max_length=20,default="")
    emp_email = models.EmailField()
    emp_mobile = models.CharField(max_length=12)
    emp_address = models.TextField(max_length=200)


    def __str__(self):
        return "Emp_id : "+self.emp_id