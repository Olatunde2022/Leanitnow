from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=40)
    Body = models.CharField(max_length=10000,null=False)
   