from django.urls import path
from myapp import views

urlpatterns = [
   path('project/create', views.projectcreate),
   path('project/show', views.projectshow),
   path('employee/create', views.employeecreate),
   path('employee/show', views.employeeshow),
   path('project/view/<int:id>', views.projectview, name='project/view'),
   path('project/addemployeetoproject/<int:id>', views.addemployeetoproject),
   path('project/delete/<int:id>', views.projectdelete),
   path('project/update/<int:id>', views.projectupdate),
   path('employee/view/<int:id>', views.employeeview, name='employee/view'),
   path('employee/asignprojecttoemployee/<int:id>', views.asignprojecttoemployee),
   path('employee/update/<int:id>', views.employeeupdate),
   path('employee/delete/<int:id>', views.employeedelete)
]