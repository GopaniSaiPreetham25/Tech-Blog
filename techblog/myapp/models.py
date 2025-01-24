from django.db import models

# Create your models here.
<<<<<<< HEAD


=======
class techblog(models.Model):
    title=models.CharField(max_length=100)
    discription=models.TextField() 
    photo=models.ImageField(upload_to='pics') 
>>>>>>> dda7f2ee6e3acac1be03fafd9e3f57406005d621
