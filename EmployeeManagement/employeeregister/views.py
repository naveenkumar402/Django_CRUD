from django.shortcuts import render, redirect
from .models import Employee


def addemployee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        if Employee.objects.filter(email=email).exists :
            return render(request, 'add_employee.html', {'error_message': 'Email already exists'})
        Employee.objects.create(name=name, email=email, mobile=mobile)
        return redirect('view_employee')  
    return render(request, 'add_employee.html')  

def viewemployee(request):
    employees = Employee.objects.all()
    return render(request, 'view_employee.html', {'employees': employees})

def deleteemployee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('view_employee')  
    return render(request, 'delete_employee.html', {'employee': employee})
