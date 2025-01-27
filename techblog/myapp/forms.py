from django import forms
from .models import techblog

class techblogForm(forms.Form): 
    class Meta:
        model = techblog
        fields ="__all__" 
