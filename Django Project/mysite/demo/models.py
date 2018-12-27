from django.db import models

# Create your models here.
class LoginUser(models.Model):
    name = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    account = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img')
    data = models.FileField(upload_to='myfile')