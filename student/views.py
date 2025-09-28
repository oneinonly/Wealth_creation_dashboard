from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student,teachers,facalty,registration
from django.contrib.auth.hashers import make_password

# Create your views here.

def student_home(request):
    data=Student.objects.all()
    print(data)
    
    # return HttpResponse("Welcome to the Student Home Page")
    return render(request,'student.html',{'data':data})

def teacher_home(request):
    data=teachers.objects.all()
    print(data)
    
    # return HttpResponse("Welcome to the Student Home Page")
    return render(request,'student.html',{'data':data})

def facalty_home(request):
    data=facalty.objects.all()
    print(data)
    # return HttpResponse("Welcome to the Student Home Page")
    return render(request,'student.html',{'data':data})

def base_home(request):
    return render (request,'home.html')

def Registration_home(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        userEmail = request.POST.get('userEmail')
        userMobile = request.POST.get('userMobile')
        password =request.POST.get('password')
        print(userName,userEmail,userEmail,userMobile, password)
        
        data=registration(name=userName, email=userEmail, mobile=userMobile, password=make_password(password))
        data.save()

    return render (request, 'registration.html' )
