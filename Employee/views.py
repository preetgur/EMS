from django.shortcuts import render , redirect,HttpResponse
from Employee.forms import Emp_form
from Employee.models import Employee


# Create your views here.


def emp(request):
    if request.method == "POST":
        # initiate form
        form = Emp_form(request.POST)
        
        if form.is_valid():
            try :
            
                form.save()
                return redirect("/show")

            except:
                print("some error occured")    
        
        else :
            return HttpResponse("Employed id alreday exits!")
    else :
        form = Emp_form()
        return render(request,"Employee/index.html",{"form_html":form})


def show(request):
    all_emp = Employee.objects.all()

    return render(request,"Employee/show.html",{"all_emp":all_emp})


def edit(request,id):
    employee = Employee.objects.get(id = id)

    return render(request,"Employee/edit.html",{"employee":employee})


def update(request,id):


    employee = Employee.objects.get(id=id)  
    # filled the form with selected employee
    print(employee)
    form = Emp_form(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  

    else : 
        print("error")    
    return render(request, 'Employee/edit.html', {'employee': employee}) 



def destroy(request,id):
    emp_del = Employee.objects.get(id = id)
    emp_del.delete()

    return redirect("/show")



def basic(request):
    return render(request,"Employee/basic.html")