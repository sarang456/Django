from django.shortcuts import render

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