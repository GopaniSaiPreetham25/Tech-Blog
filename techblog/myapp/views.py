from django.shortcuts import render

from .models import techblog
from .forms import techblogForm

def techblog_list(request):
    techblogs = techblog.objects.all()
    return render(request, 'techblog/techblog_list.html', {'techblogs': techblogs})
