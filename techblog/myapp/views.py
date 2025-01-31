from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def blog(request):
    if request.method == 'POST':
        form = techblogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:main')
    tb=techblogForm()
    return render(request,'blog.html',{'form':tb})






# from django.shortcuts import render, redirect
# from .forms import *

# def blog(request):
#     if request.method == 'POST':
#         form = techblogForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Redirect to the desired URL pattern name or another page
#             return redirect('main')  # Replace 'main' with the correct name of your URL pattern
#     else:
#         form = techblogForm()

#     # Pass the form to the template context
#     return render(request, 'blog.html', {'form': form})

 


# def update(request,id):
#     obj=techblog.objects.get(id=id)
#     if request.method == 'POST':
#         form=techblogForm(request.POST,request.FILES)
#         form=techblog(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('myapp:main')
#     tb=techblogForm(instance=obj)
#     return render(request,'update.html',{'form':tb})

# def delete(request,id):
#     tech=techblog.objects.get(id=id)
#     tech.delete()
#     return redirect('myapp:main')

def home(request):
    return render(request,'home.html')


@login_required
def main(request):
    data=techblog.objects.all()
    return render(request,'main.html',{'data':data})

def login(request):
    l1=loginForm()
    if request.method='POST':
        l1=loginForm(request.POST)
        if l1.is_valid():
            username=l1.cleaned_data.get('username')
            password=l1.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user):
                return redirect('myapp:main')
            else:
                return HttpResponse("Invalid username and password")
    return render(request,'login.html',{'form':l1})




from django.shortcuts import render,redirect
from .models import *
from .forms import CreateAccountForm

def createacc(request):
    if request.method == 'POST':
        form1=CreateAccountForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('myapp:main')
    else:
        form1 = CreateAccountForm()
    return render(request, "createacc.html", {'form': form1})



