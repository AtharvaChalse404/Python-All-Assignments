# views.py
from django.shortcuts import render
from django.db.models import Q
from .models import Employee

def employee_search(request, field, lookup, search_string):
    # Query the database based on the field and lookup options
    if field == 'empname':
        if lookup == 'startswith':
            employees = Employee.objects.filter(fname__startswith=search_string)
        elif lookup == 'contains':
            employees = Employee.objects.filter(fname__contains=search_string)
    elif field == 'empage':
        if lookup == 'lte':
            employees = Employee.objects.filter(age__lte=search_string)

    # Render the template with search results
    return render(request, 'employee_search.html', {'employees': employees})

# Define models
from django.db import models

class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fname} {self.lname}"



# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('empapp/<str:field>/<str:lookup>/<str:search_string>/', views.employee_search, name='employee_search'),
]



''' <!-- employee_search.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Employee Search Results</title>
</head>
<body>
    <h1>Employee Search Results</h1>
    <ul>
        {% for employee in employees %}
            <li>{{ employee.fname }} {{ employee.lname }}, Age: {{ employee.age }}, Address: {{ employee.address }}</li>
        {% empty %}
            <li>No employees found.</li>
        {% endfor %}
    </ul>
</body>
</html>
'''