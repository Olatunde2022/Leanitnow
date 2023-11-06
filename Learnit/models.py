from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Review(models.Model):
#     # user=models.OneToOneField(User,on_delete=models.CASCADE)
#     Name = models.CharField(max_length=40)
#     Email = models.CharField(max_length=40)
#     Nationality = models.CharField(max_length=15)
#     Body = models.CharField(max_length=10000)

class myReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Nationality = models.CharField(max_length=15)
    Body = models.CharField(max_length=10000)
   