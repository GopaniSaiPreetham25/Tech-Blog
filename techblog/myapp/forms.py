from django import forms
from .models import techblog

from django.contrib.auth.models import User

<<<<<<< HEAD
# forms.py
 # Replace with your actual model

class CreateAccountForm(forms.ModelForm):
=======
class createaccountForm(forms.ModelForm):
>>>>>>> f63e2532fa690bf2cb27ff3d6d3753b08b532412
    class Meta:
        model = User
        fields=['username','first_name','last_name','password']

class techblogForm(forms.Form): 
    class Meta:
        model = techblog
        fields='__all__'
