from django.shortcuts import render, redirect
from .forms import Service_form
from .models import service

def studenthome(request):
    return render(request,'student/studenthome.html')
def student_dashbord(request):
    student ={
        "name":"Krish",
        "age":22,
        "en_No":1234567 
    }
    return render(request, 'student/student_dashbord.html', student)

def noti(request):
    return render(request, 'student/notification.html')
    
def scholer(request):
    incharge = {
        "Prof1":"S. C. Category",
        "Prof2":"S. C. Category",
        "Prof3":"O.B. C. Category",
        "Prof4":"Vacharati Mukt Stri Category",
        "Prof5":"S. T. Category"
    }
    return render(request, 'student/scholership.html', incharge)

def useful(request):
    link = {
        "Website1":"www.gecpt.cteguj.in",
        "Website2":"hostelgecp.blogspot.com",
        "Website3":"gtu.ac.in",
    }
    return render(request, 'student/useful.html', link)

def service_list(request):
    services = service.objects.all()
    return render(request, "student/service_list.html", {"services" : services})

def service_create(request):
    if request.method == "POST":
        form = Service_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student:list")
        else:
            return render(request, "student/service_create.html", {"form" : form})    
    else:
        form = Service_form()
        return render(request, "student/service_create.html", {"form" : form})
    

def service_update(request, id):
    serv = service.objects.get(id=id)
    form = Service_form(request.POST, instance=serv)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("student:list")
        else:
            return render(request, "student/service_create.html", {"form" : form})
    else:
        form = Service_form(instance=serv)
        return render(request, "student/service_create.html", {"form" : form})
    

def service_delete(request, id):
    service.objects.filter(id=id).delete()
    return redirect("student:list")