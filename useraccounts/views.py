from django.shortcuts import render,redirect, get_object_or_404
from . form import RegistrationForm, userloginForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User




# Create your views here.
@login_required
def home(request):
    users= User.objects.all()
    

    return render(request, 'auth/dashboard.html', {"users":users})


def registration(request):
    form=RegistrationForm(request.POST)
    if form.is_valid():
        user=form.save()
        login (request, user)
        return redirect('dashboard')
    else:
        form=RegistrationForm()
    return render(request,'auth/registration.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    form=userloginForm(request.POST)
    if form.is_valid():
        username= form.cleaned_data['username']
        password=form.cleaned_data['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            form.add_error(None, "invalid credentials")
    else:
        form=userloginForm()
    return render(request,"auth/login.html", {'form':form})


def delete_user(request, pk):
    user= get_object_or_404(User, pk=pk)
    if user is not None:
        user.delete()
        return redirect( 'dashboard')

        
