from django.db import models
class Employee(models.Model):
    firstName = models.CharField(max_length=100)  
    lastName = models.CharField(max_length=100)  
    employeeId = models.CharField(max_length=20)  
    city = models.CharField(max_length=20)  

