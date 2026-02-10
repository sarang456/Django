from django.urls import path
from.import views
urlpatterns = [
    path('employe_details/', views.empdetails),
    path('employe_filter/', views.employeeFilter)
]