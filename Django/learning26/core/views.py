from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.
def registerUser(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empdetail")
    else:
        form = UserForm()

    return render(request,"core/registeruser.html", {'form':form})