from django.shortcuts import render
from empapp.models import Employee

# Create your views here.

def employeedata(request):
    emp=Employee.objects.all()
    empdict={'employee':emp}
    return render(request,"emp.html",empdict)
