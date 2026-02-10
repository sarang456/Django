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