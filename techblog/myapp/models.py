from django.db import models

# Create your models here.

class techblog(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField() 
    photo=models.ImageField(upload_to='pics')
    

