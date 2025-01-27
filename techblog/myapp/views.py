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
 
def main(request):
    data=techblog.objects.all()
    return render(request,'main.html',{'data':data})

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

def createaccount(request):
    if request.method == 'POST':
        form=CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:main')
    else:
        form = CreateAccountForm()
    return render(request, "createaccount.html", {'form': form})
