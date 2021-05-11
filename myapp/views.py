from django.shortcuts import render, redirect

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
        employee = EmployeeForm(request.POST)
        employee.save()
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
        pro = ProjectForm(request.POST, instance=project)
        pro.save()
        return redirect('/myapp/project/view')
    else:
        emp = Employee.objects.all()
        pro = Project.objects.get(id = id)
        return render(request, 'myapp/addemployeetoproject.html', {'emp': emp, 'pro': pro})



# Create your views here.
