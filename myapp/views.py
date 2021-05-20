from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse

from myapp.form import ProjectForm, EmployeeForm
from myapp.models import Project, Employee


def home(request):
    return render(request, 'myapp/home.html')

def projectcreate(request):
    if request.method == 'POST':
        project = ProjectForm(request.POST)
        project.save()
        return redirect('/myapp/project/show')
    else:
        pro = ProjectForm
        return render(request, 'myapp/projectcreate.html', {'pro': pro})

def employeecreate(request):
    if request.method == 'POST':
        emp = EmployeeForm(request.POST)
        if emp.is_valid():
            emp.save()
            messages.success(request, 'Employee created')
            return redirect('/myapp/employee/show')
    else:
        emp = EmployeeForm
    return render(request, 'myapp/employeecreate.html', {'emp': emp})

def employeeshow(request):
    list = Employee.objects.all()
    return render(request, 'myapp/employeeshow.html', {'list': list})

def projectshow(request):
    list = Project.objects.all()
    return render(request, 'myapp/projectshow.html', {'list': list})

def projectview(request, id):
    pro = Project.objects.get(id = id)
    return render(request, 'myapp/projectview.html', {'pro': pro})

def addemployeetoproject(request, id):
    if request.method == 'POST':
        project = Project.objects.get(id = id)
        list = request.POST.getlist('employees')
        project.employees.clear()
        for p in list:
            e = Employee.objects.get(id=p)
            project.employees.add(e)
        return redirect('project/view', id=id)
    else:
        emp = Employee.objects.all()
        pro = Project.objects.get(id = id)
        return render(request, 'myapp/addemployeetoproject.html', {'emp': emp, 'pro': pro})

def projectdelete(request, id):
    pro = Project.objects.get(id=id)
    pro.delete()
    return redirect('/myapp/project/show')

def projectupdate(request, id):
    if request.method == 'POST':
        pro = Project.objects.get(id=id)
        pro.name = request.POST['name']
        pro.type = request.POST['type']
        pro.save()
        return redirect('/myapp/project/show')
    else:
        pro = Project.objects.get(id=id)
        return render(request, 'myapp/projectupdate.html', {'pro': pro})

def employeeview(request, id):
    emp = Employee.objects.get(id=id)
    return render(request, 'myapp/employeeview.html', {'emp': emp})

def asignprojecttoemployee(request, id):
    if request.method == 'POST':
        emp = Employee.objects.get(id=id)
        list = request.POST.getlist('project')
        emp.projects.clear()
        for e in list:
            p = Project.objects.get(id = e)
            emp.projects.add(p)
       # return redirect('view', id=id)
        return redirect('employee/view', id = id)
    else:
        emp = Employee.objects.get(id=id)
        pro = Project.objects.all()
        return render(request, 'myapp/asignprojecttoemployee.html', {'emp': emp, 'pro': pro})

def employeeupdate(request, id):
    if request.method == 'POST':
        emp = Employee.objects.get(id=id)
        emp.name = request.POST['name']
        emp.city = request.POST['city']
        emp.save()
        return redirect('/myapp/employee/show')
    else:
        emp = Employee.objects.get(id=id)
        return render(request, 'myapp/employeeupdate.html', {'emp': emp})

def employeedelete(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/myapp/employee/show')





# Create your views here.
