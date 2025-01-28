from django import forms
from .models import techblog

class techblogForm(forms.Form): 
    class Meta:
        model = techblog
        fields =['title','discription','photo']

from django.contrib.auth.models import User

# forms.py
 # Replace with your actual model

class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['email','first_name','last_name','password']


