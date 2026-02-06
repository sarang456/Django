from django.contrib import admin
from .models import Student, product, internship, Course, service, category, student_profile, vehicle, vehicleRegistration, ServiceRecord, InsurancePolicy, TrafficFine, AccidentReport


admin.site.register(Student)
admin.site.register(product)
admin.site.register(internship)
admin.site.register(Course)
admin.site.register(student_profile)
admin.site.register(service)
admin.site.register(category)
admin.site.register(vehicle)
admin.site.register(AccidentReport)
admin.site.register(TrafficFine)
admin.site.register(InsurancePolicy)
admin.site.register(ServiceRecord)
admin.site.register(vehicleRegistration)