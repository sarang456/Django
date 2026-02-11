from django.contrib import admin
from .models import employee, Course, product, vehicle

# Register your models here.
admin.site.register(employee)
admin.site.register(Course)
admin.site.register(product)
admin.site.register(vehicle)