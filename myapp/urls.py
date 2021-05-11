from django.urls import path
from myapp import views

urlpatterns = [
   path('project/create', views.projectcreate),
   path('project/show', views.projectshow),
   path('employee/create', views.employeecreate),
   path('employee/show', views.employeeshow),
   path('project/view/<int:id>', views.projectview),
   path('project/addemployeetoproject/<int:id>', views.addemployeetoproject),
]