from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import techblog
from .forms import *
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required


def blog(request):
    if request.method == 'POST':
        form = techblogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:main')
    else:
        form = techblogForm()
    posts = techblog.objects.all().order_by('-id')  
    return render(request, 'blog.html', {'form': form, 'posts': posts})

@login_required
def main(request):
    data = techblog.objects.all()
    return render(request, 'main.html', {'data': data})

def post_detail(request, post_id):
    post = get_object_or_404(techblog, id=post_id)  
    return render(request, 'post_detail.html', {'post': post})

def home(request):
    return render(request, 'home.html')



from django.contrib.auth import authenticate, login,logout # Import login function
from django.shortcuts import render, redirect
from django.contrib import messages

def loginview(request):
    l1 = loginForm()
    if request.method == 'POST':
        f1 = loginForm(request.POST)
        if f1.is_valid():
            username = f1.cleaned_data.get('username')  # Make sure you're using 'username', not 'email'
            password = f1.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('myapp:main')
            else:
                messages.error(request, "Invalid username or password")
    return render(request, 'login.html', {'form': l1})

    
def logoutview(request):
    logout(request)
    return redirect('myapp:login')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def createacc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check if passwords match
        if password != confirm_password:
            return render(request, 'createacc.html', {'error': 'Passwords do not match'})

        # Hash the password before saving
        hashed_password = make_password(password)

        # Create the user with the hashed password
        user = User(username=username, password=hashed_password)
        user.save()

        # Redirect to login or another page
        return redirect('myapp:login')
    return render(request, 'createacc.html')




def update(request, id):
    obj = get_object_or_404(techblog, id=id)
    if request.method == 'POST':
        form = techblogForm(request.POST, request.FILES, instance=obj)  
        if form.is_valid():
            form.save()
            return redirect('myapp:main')
    else:
        form = techblogForm(instance=obj)
    return render(request, 'update.html', {'form': form})

def delete(request, id):
    tech = get_object_or_404(techblog, id=id)
    tech.delete()
    return redirect('myapp:main')

def about(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'about.html', context)






