from django.db import models
from django.contrib.auth.models import User

    
class myCourse(models.Model):   
    coursename = models.CharField(max_length=500,  null=True, blank=True)  
    def __str__(self):
        return f"{self.coursename}-{self.id}"
    
        
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50,null=True,blank=True )
    studentcourse = models.ManyToManyField(myCourse)
    
    
    
# class StudentCourse(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(myCourse, on_delete=models.CASCADE)
    

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
    
    
class Proof(models.Model):
    receipt = models.ImageField()
    student = models.ForeignKey(Student,null=True,blank=True,on_delete=models.CASCADE)
    uploadDateTime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"No:{self.id} uploaded by {self.student} at {self.uploadDateTime}"
    
    
    
# class Course(models.Model):
#    course_name = models.CharField(max_length=50)
#    question_number = models.PositiveIntegerField()
#    total_marks = models.PositiveIntegerField()
#    def __str__(self):
#         return self.course_name

# class Question(models.Model):
#     course=models.ForeignKey(Course,on_delete=models.CASCADE)
#     marks=models.PositiveIntegerField()
#     question=models.CharField(max_length=600)
#     option1=models.CharField(max_length=200)
#     option2=models.CharField(max_length=200)
#     option3=models.CharField(max_length=200)
#     option4=models.CharField(max_length=200)
#     cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
#     answer=models.CharField(max_length=200,choices=cat)

# class Result(models.Model):
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     exam = models.ForeignKey(Course,on_delete=models.CASCADE)
#     marks = models.PositiveIntegerField()
#     date = models.DateTimeField(auto_now=True)

    
    
    

    
    
    
    