from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student,teachers,facalty

# Create your views here.

def student_home(request):
    data=Student.objects.all()
    print(data)
    
    # return HttpResponse("Welcome to the Student Home Page")
    return render(request,'home.html',{'data':data})

def teacher_home(request):
    data=teachers.objects.all()
    print(data)
    
    # return HttpResponse("Welcome to the Student Home Page")
    return render(request,'teacher.html',{'data':data})

def facalty_home(request):
    data=facalty.objects.all()
    print(data)
    
    # return HttpResponse("Welcome to the Student Home Page")
    return render(request,'facalty.html',{'data':data})

def base_home(request):
    return render (request,'base.html')