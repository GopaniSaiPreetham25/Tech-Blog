from django.shortcuts import render,redirect
from .models import techblog
from .forms import techblogForm

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

def home(request):
    return render(request,'p2.html')

def login(request):
    return render(request,'p1.html')