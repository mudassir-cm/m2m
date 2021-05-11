from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=29)
    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=29)
    employees = models.ManyToManyField(Employee, related_name='projects')

    def __str__(self):
        return self.name



# Create your models here.
