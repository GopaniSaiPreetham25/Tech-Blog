from django import forms
from .models import *

class techblogForm(forms.ModelForm): 
    class Meta:
        model = techblog
        fields =['title','discription','photo']




from django.contrib.auth.models import User

class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['email','first_name','last_name','password']

