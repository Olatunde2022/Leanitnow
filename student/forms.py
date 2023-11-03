from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserChangeForm
from .models import Student, myCourse
from django.forms import ModelMultipleChoiceField, ModelForm
# from quiz import models as QMODEL

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password', 'email'] 
        widgets = {
        'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields=['address','mobile','profile_pic']
        
# class (forms.ModelForm):
#     courseName = ModelMultipleChoiceField(queryset=Student.objects.all())    
#     class Meta:
#         model = myCourse
#         fields = ['courseName']


class EditUserProfileForm(UserChangeForm):
    username = forms.CharField( required=True, widget=forms.TextInput(attrs = {"class": "form-control", "placeholder":"Enter your new username"}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs = {"class": "form-control", "placeholder":"Enter your correct first name"}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs = {"class": "form-control", "placeholder":"Enter your correct flast name"}))
    mobile = forms.IntegerField(required=True, widget=forms.TextInput(attrs = {"class": "form-control", "placeholder":"Enter your new number"}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs = {"class": "form-control", "placeholder":"Enter your new address"}))
    profile_pic = forms.ImageField(allow_empty_file=True,  widget=forms.FileInput(attrs = {"class": "form-control"}))    
    password = forms.PasswordInput()
   
    class Meta:       
        model=models.Student
        fields=['address','mobile','profile_pic']
        
    class Meta:
        model = User
        fields = ["username","first_name", "last_name"]
        