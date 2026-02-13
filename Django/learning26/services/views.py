from django.shortcuts import render, redirect, HttpResponse
from .models import service
from .forms import Service_form

def service_list(request):
    list = service.objects.all().order_by("id").values()
    return render(request, "service/service_list.html", {"list" : list})

def create_service(request):
    if request.method == "POST":
        form = Service_form(request.POST)
        form.save()
        return redirect('list')
    else:
        form = Service_form()
        return render(request, "service/create_service.html", {"form" : form})
    
def service_update(request, id):
    service_det = service.objects.get(id=id)
    if request.method == "POST":
        update_form = Service_form(request.POST, instance=service_det)
        update_form.save()
        return redirect('list')
    else:
        update_form = Service_form(instance=service_det)
        return render(request, "service/update_service.html", {"form" : update_form})
    
def service_delete(request, id):
    delete_ser = service.objects.filter(id=id).delete()
    return redirect("list")