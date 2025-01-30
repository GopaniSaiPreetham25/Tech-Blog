from django.db import models
from django.contrib.auth.models import User


class techblog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    photo = models.ImageField(upload_to='pics/',null=True,blank=True)
    likes = models.PositiveIntegerField(default=0)
<<<<<<< HEAD
    title=models.CharField(max_length=100)
    discription=models.TextField() 
    photo=models.ImageField(upload_to='pics') 
# class techblog(models.Model):
#     title=models.CharField(max_length=100)
#     discription=models.TextField() 
#     photo=models.ImageField(upload_to='pics')
    


=======
    
>>>>>>> 3aa15211ea1d3879558ea68e4410940506259515
class Comment(models.Model):
    post = models.ForeignKey(techblog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
