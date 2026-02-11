from django.urls import path
from.import views
urlpatterns = [
    path('employe_details/', views.empdetails),
    path('employe_filter/', views.employeeFilter),
    path('createemploye/', views.createEmploye),
    path('emp_form/', views.Emp_Form),
    path('courese/', views.course),
    path('product/', views.product),
    path('vehicle/', views.vehicle)
]