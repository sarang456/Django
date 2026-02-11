from django.db import models

# Create your models here.
class employee(models.Model):
    Emp_Name = models.CharField(max_length=100)
    Emp_Salary = models.FloatField()
    Emp_Joining_Date = models.DateField(auto_now_add=True)
    Emp_Age = models.IntegerField()
    Emp_Post = models.CharField(max_length=100)

    class meta:
        db_table = "Employee" 

    def __str__(self):
        return self.Emp_Name
    
class Course(models.Model):
    cource_name = models.CharField(max_length=50)
    Course_code = models.CharField(max_length=50)
    Duration = models.IntegerField()
    Fees = models.IntegerField()
    Is_active = models.BooleanField(default=True)

    class meata:
        db_table = "course"

    def __str__(self):
        return self.cource_name
    
class product(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_color = models.CharField(max_length=100)
    Product_price = models.IntegerField()
    Product_stock = models.PositiveIntegerField()
    
    class meta:
        db_table = "product"
    
    def __str__(self):
        return self.Product_name

class vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)
    fule = (("Petrol", "Petrol"), ("Diesel", "Diesel"), ("CNG", "CNG"), ("Electric", "Electric"), ("Hybrid", "Hybrid"))
    vehicle_manufacture = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    vehicle_fule = models.CharField(max_length=100, choices=fule)
    vehicle_engine_no = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=30)

    class Meta:
        db_table = "Emp_vehicle"

    def __str__(self):
        return self.vehicle_name