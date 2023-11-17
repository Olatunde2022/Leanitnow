from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import myReview
from student.models import Student

# Create your views here.
def Index(request):
    
    if request.method == 'POST':
        form = request.POST
        Name = form.get('Name')
        Email = form.get('Email')
        Nationality = form.get('Nationality')
        Body = form.get('Body')       
        if request.user.is_authenticated:
            student = request.user.student
        else:
            student = None
            
        review = myReview.objects.create(Name=Name, Email=Email, Nationality = Nationality, Body = Body, student=student)
        review.save()
        messages.success(request, 'Thanks for reviewing us')
        # return render(request, 'Learnit/index.html')
    user = request.user
    
    fetch_review = myReview.objects.all()
    # for Review in fetch_review:
    #     context = {'Review':Review}
    context = {'Reviews': fetch_review, "user":user}
    if request.user.is_authenticated:
        student_exit = Student.objects.filter(user=user).exists()
        if student_exit:
            student = Student.objects.get(user=user)
            fetch_review = myReview.objects.all()
            context = {'Reviews': fetch_review, "student": student, "user":user}
        else:
            context = {'Reviews': fetch_review, "user":user}
        return render(request, 'Learnit/index.html', context) 
    # context = {'Review': fetch_review, "student": student, "user":user}
    return render(request, 'Learnit/index.html', context)

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