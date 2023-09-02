from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments
def index(request):
    person = {
        'name' : 'binsha',
        'age' :25,
        'place' : 'ernakulam'
    }
    return render(request,'index.html',person)
def about(request):
    return render(request,'about.html')
def booking(request):
    return render(request,'booking.html')
def doctors(request):
    return render(request,'doctors.html')
def contact(request):
    return render(request,'contact.html')
def department(request):
    dict_dept = {
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)

# Create your views here.
