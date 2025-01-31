from django import forms
from .models import *

class techblogForm(forms.ModelForm): 
    class Meta:
        model = techblog
        fields =['title','discription','photo']




from django.contrib.auth.models import User
<<<<<<< HEAD

=======
>>>>>>> 3035bc642fcff0227c82426395ac30839a96201c
class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['email','first_name','last_name','password']

