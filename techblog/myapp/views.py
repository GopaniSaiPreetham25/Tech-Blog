from django.shortcuts import render

from .models import techblog
from .forms import techblogForm


def techblog(request):
    return render(request, 'techblog.html', {'techblogs': techblogs})
