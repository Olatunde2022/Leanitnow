from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import myReview
from student.models import Student

# Create your views here.
def Index(request):
    user = request.user
    
    if request.method == 'POST':
        form = request.POST
        Name = form.get('Name')
        Email = form.get('Email')
        Nationality = form.get('Nationality')
        Body = form.get('Body')
        
        review = myReview.objects.create(Name=Name, Email=Email, Nationality = Nationality, Body = Body)
        review.save()
        messages.success(request, 'Thanks for reviewing us')
        return render(request, 'Learnit/index.html')
    
    if request.user.is_authenticated:
        fetch_review = myReview.objects.all()
        student_exit = Student.objects.filter(user=user).exists()
        if student_exit:
            student = Student.objects.get(user=user)
            context = {'Review': fetch_review, "student": student, "user":user}
        else:
            context = {'Review': fetch_review, "user":user}
        return render(request, 'Learnit/index.html', context) 
    return render(request, 'Learnit/index.html')

def Courses(request):
    return render(request, 'Learnit/courses.html')

def Contact(request):
    return render(request, 'Learnit/contact.html')

def About(request):
    return render(request, 'Learnit/about.html')

# def Reviews(request):
#     if request.method == 'POST':
#         form = request.POST
#         Name = form.get('Name')
#         Email = form.get('Email')
#         Nationality = form.get('Nationality')
#         Body = form.get('Body')
        
#         review = myReview.objects.create(Name=Name, Email=Email, Nationality = Nationality, Body = Body)
#         review.save()
#         messages.success(request, 'Thanks for reviewing us')
#         return redirect(reverse(request, 'Learnit_Index_page'))      
#     return render(request, 'Learnit/index.html')