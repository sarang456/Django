from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_Enroll = models.CharField(max_length=15)
    student_age = models.PositiveIntegerField()
    student_Email = models.EmailField(null=True)

    class Meta:
        db_table = "student"


class product(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_color = models.CharField(max_length=100)
    Product_price = models.IntegerField()
    Product_stock = models.PositiveIntegerField()
    
    class meta:
        db_table = "product"
class internship(models.Model):
    company_name = models.CharField(max_length=50)
    internship_role = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)

    class meta:
        db_table = "internship"

class Course(models.Model):
    cource_name = models.CharField(max_length=50)
    Course_code = models.CharField(max_length=50)
    Duration = models.IntegerField()
    Fees = models.IntegerField()
    Is_active = models.BooleanField(default=True)

    class meata:
        db_table = "course"