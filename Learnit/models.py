from django.db import models
from django.contrib.auth.models import User
from student.models import Student

# Create your models here.

class myReview(models.Model):
    student = models.ForeignKey(Student,on_delete=models.PROTECT, null=True,blank=True)
    Name = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    Nationality = models.CharField(max_length=15)
    Body = models.CharField(max_length=10000)
    
    def __str__(self):
        return f"{self.id}--Review created by {self.student}"
    
   