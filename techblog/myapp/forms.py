from django import forms
from .models import techblog

from django.contrib.auth.models import User

class CreateaccountForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']

class techblogForm(forms.Form): 
    class Meta:
        model = techblog
        fields='__all__'
