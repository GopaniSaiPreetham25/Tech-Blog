from django.shortcuts import render, redirect, get_object_or_404
from .models import techblog
from .forms import techblogForm, CreateAccountForm
from django.shortcuts import render
from datetime import datetime

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

def main(request):
    data = techblog.objects.all()
    return render(request, 'main.html', {'data': data})

def post_detail(request, post_id):
    post = get_object_or_404(techblog, id=post_id)  
    return render(request, 'post_detail.html', {'post': post})

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def createacc(request):
    if request.method == 'POST':
        form1 = CreateAccountForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('myapp:main')
    else:
        form1 = CreateAccountForm()
    return render(request, "createacc.html", {'form': form1})

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
from django.shortcuts import render
from datetime import datetime

def about(request):
    context = {
        'year': datetime.now().year
    }
    return render(request, 'about.html', context)
