from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *

def insert(request):
    if request.method == 'POST':
        form = techblogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:viewdata')
    tb=techblogForm()
    return render(request,'insert.html',{'form':tb})
 
def viewdata(request):
    data=techblog.objects.all()
    return render(request,'viewdata.html',{'data':data})

def update(request,id):
    obj=techblog.objects.get(id=id)
    if request.method == 'POST':
        form=techblog(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:viewdata')
    tb=techblogForm(instance=obj)
    return render(request,'update.html',{'form':tb})

def delete(request,id):
    tech=techblog.objects.get(id=id)
    tech.delete()
    return redirect('myapp:viewdata')

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
<<<<<<< HEAD

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateAccountForm

def createaccount(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Account is created</h1>')
    else:
        form = CreateAccountForm()
    return render(request, "createaccount.html", {'form': form})

=======

def createaccount(request):
    r1=createaccount()
    if request.method=='POST':
        r1=createaccount(request.POST)
        if r1.is_valid(): 
            r1.save()
            return HttpResponse('<h1> Account is created </h1>')    
    return render(request,"createaccount.html",{'form':r1})
   
>>>>>>> f63e2532fa690bf2cb27ff3d6d3753b08b532412
