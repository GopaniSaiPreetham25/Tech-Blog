from django.db import models


class techblog(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField() 
    photo=models.ImageField(upload_to='pics')

