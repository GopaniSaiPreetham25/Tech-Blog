from django.db import models
# Create your models here.

<<<<<<< HEAD

class techblog(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField() 
    photo=models.ImageField(upload_to='pics') 
=======
class techblog(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField() 
    photo=models.ImageField(upload_to='pics')
    


>>>>>>> 96d77dd48caa8ca1dba73de9bedf015b0a8cf559
