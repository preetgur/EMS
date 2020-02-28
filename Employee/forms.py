from django import forms
from Employee.models import Employee

class Emp_form(forms.ModelForm):

    class Meta:
        model = Employee
        fields = "__all__"