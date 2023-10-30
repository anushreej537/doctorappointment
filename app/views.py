from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        user_type = request.POST['usercheck']
        if User.objects.filter(email=email).exists():
            return redirect('/signup/')

        else:
            User.objects.create(name=name,email=email,password=password,user_type=user_type)
            messages.error(request,'successfully registered')
            return redirect('/login/')
    else:
        return redirect('/signup/')

def login(request):
    return render(request,'login.html')
        
def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            if check_password(user_password,password):
                if obj.user_type=='doctor':
                    return redirect('/dashboard/')
                else:
                    return redirect('/table/')
            else:
                messages.error(request,'invalid password')
                return redirect('/login/')
        else:
            messages.error(request,'email not correct')
            return redirect('/login/')


def dashboard(request):
    data1 = Doctor.objects.all()
    return render(request,'dashboard.html',{'data1':data1})

# def table(request):
#     return render(request,'table.html')

def admin_data(request):
    if request.method == 'POST':
        drname = request.POST['drname']
        date = request.POST['date']
        daytime = request.POST['time']
        speciality = request.POST['speciality']
        Doctor.objects.create(drname=drname,date=date,daytime=daytime,speciality=speciality)
    data1 = Doctor.objects.all()
    return render(request,'admin_view.html',{'data1':data1})
    