from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

def fun(request):
    return HttpResponse("<h1> Students </h1>")
def index(request):
    return HttpResponse("Hello world, This ia my first django project")

"""Only dictionary can be passed as argument in django """
def my_view(request):
    a={"title":"Python"}
    return render(request,'index.html',a)

"""passing list using dictionary in django"""
def list(request):
    a=[10,20,30,40,50]
    dict={"list":a}
    return render(request,"list.html",dict)

"""get data from form and display"""
def form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        return HttpResponse(f"Received username: {username}, Received email: {email}")
    return render(request,"form.html")

'''Store user data in database using [python manage.py makemigrations(make changes), python manage.py migrate(connect database)]'''
from .models import Person
def add_db(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        Person.objects.create(name=name, age=age)
        return HttpResponseRedirect('/success')
    return render(request,'add_db.html')

def success(request):
    persons = Person.objects.all()
    print(persons)
    return render(request,"success.html",{"persons":persons})

'''Redirect and return from function and resume it'''
def fun4(request):
    a=100
    return HttpResponse(a)
def fun5(request):
    new=fun4(request)
    return HttpResponse(new)
