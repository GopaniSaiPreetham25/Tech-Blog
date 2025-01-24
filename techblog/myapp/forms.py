from django import forms
from .models import techblog

class techblogForm(forms.Form): 
    class Meta:
        model = techblog
<<<<<<< HEAD
        fields ="__all__" 

=======
        fields ="__all__"
 
>>>>>>> 698e57127b199beb8620205aa0f403a8f95455dd
