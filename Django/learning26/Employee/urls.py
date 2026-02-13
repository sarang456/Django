from django.urls import path
from.import views
urlpatterns = [
    path('employe_details/', views.empdetails, name="empdetail"),
    path('employe_filter/', views.employeeFilter),
    path('createemploye/', views.createEmploye),
    path('emp_form/', views.Emp_Form, name="createemploye"),
    path('courese/', views.course),
    path('product/', views.product),
    path('vehicle/', views.vehicle),
    path('delete_emp/<id>', views.delete_Emp, name="Delete_Emp"),
    path('emp_filt/', views.filter_Emp_Age, name="emp_filter"),
    path('emp_asecn/', views.assending, name="asen_order"),
    path('emp_dsecn/', views.disending, name="dsen_order"),
    path('update_emp/ <id>', views.update_employe, name="updateemp")
]