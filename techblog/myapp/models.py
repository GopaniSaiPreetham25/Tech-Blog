from django.db import models

class techblog(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    photo = models.ImageField(upload_to='pics/',null=True,blank=True)
    likes = models.PositiveIntegerField(default=0)
    title=models.CharField(max_length=100)
 

from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey(techblog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()      
    created_at = models.DateTimeField(auto_now_add=True)
