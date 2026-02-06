from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_Enroll = models.CharField(max_length=15)
    student_age = models.PositiveIntegerField()
    student_Email = models.EmailField(null=True)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.student_name


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

class student_profile(models.Model):
    hobblies = (("Working", "Working"), ("Music_Listning", "Music_Listning"), ("Reading", "Reading"), ("Singing", "Singing"), ("Runnig", "Running"))
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE)
    student_hobbies = models.CharField(max_length=100, choices=hobblies)
    student_address = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=10)
    student_gender = models.CharField(max_length=10)
    student_dob = models.DateField()

    class Meta:
        db_table = "studentprofile"
    
    def __str__(self):
        return self.student_id.student_name
    

class category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()
    category_status = models.BooleanField(default=True)

    class Meta:
        db_table = "category"
    
    def __str__(self):
        return self.category_name
    
class service(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.TextField()
    service_status = models.BooleanField(default=True)
    service_discount = models.IntegerField(null=True)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    service_price = models.FloatField(null=True)

    class Meta:
        db_table = "service"

    def __str__(self):
        return self.service_name
    
class vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)
    fule = (("Petrol", "Petrol"), ("Diesel", "Diesel"), ("CNG", "CNG"), ("Electric", "Electric"), ("Hybrid", "Hybrid"))
    vehicle_manufacture = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=100)
    vehicle_fule = models.CharField(max_length=100, choices=fule)
    vehicle_engine_no = models.CharField(max_length=50)
    vehicle_color = models.CharField(max_length=30)

    class Meta:
        db_table = "vehicle"

    def __str__(self):
        return self.vehicle_name
    

class vehicleRegistration(models.Model):
    reg_name = models.CharField(max_length= 20, default=True)
    reg_date = models.DateField(default=True)
    owner_name = models.CharField(max_length=100)
    owner_address = models.TextField()
    vehicle_id = models.OneToOneField(vehicle, on_delete = models.CASCADE)

    class Meta:
        db_table = "vehicleRegistration"
    
    def __str__(self):
        return self.reg_name
    

class ServiceRecord(models.Model):
    vehicle_id = models.ForeignKey(vehicle, on_delete = models.CASCADE)
    service_date = models.DateField()
    service_center = models.CharField(max_length=100)
    cost = models.FloatField(max_length=10)

    class Meta:
        db_table = "ServiceRecord"

class InsurancePolicy(models.Model):
    vehicle_id = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=100)
    insurer_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "InsurancePolicy"

class TrafficFine(models.Model):
    vehicle_id = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    challan_number = models.CharField(max_length=100)
    issue_date = models.DateField()
    offence = models.TextField()

    class Meta:
        db_table = "TrafficFine"

class AccidentReport(models.Model):
    vehicle_id = models.ForeignKey(vehicle, on_delete=models.CASCADE)
    accident_date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    