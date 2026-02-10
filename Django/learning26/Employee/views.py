from django.shortcuts import render
from django.db.models import Q
from .models import employee

# Create your views here.
def empdetails(request):
    employe = employee.objects.all().values()
    # for emp in employe:
    
    return render(request, "employee/employe_detils.html", {"employe": employe})

def employeeFilter(request):
    emp1 = employee.objects.filter(Emp_Name = "Kishan").values_list()
    emp2 = employee.objects.filter(Emp_Post = "Researcher").values_list()
    emp3 = employee.objects.filter(Emp_Name = "Krish", id = "3").values_list()
    emp4 = employee.objects.filter(Q(Emp_Age = 24) | Q(Emp_Name = "Umang")).values_list()
    emp5 = employee.objects.filter(Emp_Age__gt = 23).values_list()
    emp6 = employee.objects.filter(Emp_Age__gte = 23).values_list()
    emp7 = employee.objects.filter(Emp_Name__exact = "kishan").values_list()
    emp8 = employee.objects.filter(Emp_Name__iexact = "kishan").values_list() #this for ingnore case sensitivite
    emp9 = employee.objects.filter(Emp_Name__contains = "k").values_list()
    emp10 = employee.objects.filter(Emp_Name__startswith='K').values_list()
    emp11 = employee.objects.filter(Emp_Name__icontains = 'k').values_list()
    emp12 = employee.objects.filter(Emp_Name__endswith = 'g').values_list()
    emp13 = employee.objects.filter(Emp_Name__in = ['Kishan', 'Umang']).values_list()
    emp14 = employee.objects.filter(Emp_Age__range= ['20', '23']).values_list()
    emp15 = employee.objects.order_by("Emp_Name").values_list()
    emp16 = employee.objects.order_by("-Emp_Name").values_list()
    emp17 = employee.objects.order_by("-Emp_Age").values_list()
    
    # print("Query1:", emp1)
    # print("Query2:", emp2)
    # print("Query3:", emp3)
    # print("Query4:", emp4)
    # print("Query5:", emp5)
    # print("Query6:", emp6)
    # print("Query7:", emp7)
    # print("Query8:", emp8)
    # print("Query9:", emp9)
    # print("Query10:", emp10)
    # print("Query11:", emp11)
    # print("Query12:", emp12)
    # print("Query13:", emp13)
    # print("Query14:", emp14)
    # print("Query15:", emp15)
    # print("Query16:", emp16)
    # print("Query17:", emp17)
    return render(request, "employee/employ_filter.html")