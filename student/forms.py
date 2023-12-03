from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserChangeForm
from .models import Student, myCourse
from django import forms
from django.contrib.auth.forms import UserCreationForm

# class PasswordResetForm(UserCreationForm):
#     field_labels = {
#         'email': 'Email',
#     }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Customize form fields and behavior here

# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(label='Email', max_length=254)

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
        fields=['address','mobile','profile_pic', 'email']
