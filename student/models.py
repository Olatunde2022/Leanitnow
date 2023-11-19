from django.db import models
from django.contrib.auth.models import User

    
class myCourse(models.Model):   
    coursename = models.CharField(max_length=500,  null=True, blank=True)  
    def __str__(self):
        return f"{self.coursename}"
    
        
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,null=True,blank=True )
    studentcourse = models.ManyToManyField(myCourse)
    
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    
class Proof(models.Model):
    receipt = models.ImageField()
    student = models.ForeignKey(Student,null=True,blank=True,on_delete=models.CASCADE)
    uploadDateTime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"No:{self.id} uploaded by {self.student} at {self.uploadDateTime}"
    
   
    