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
        
        
        # if not Name or not Nationality or not Body or not Email:
        #     messages.error(request, "There is imcomplete field(s)")
        #     return redirect(reverse(request, 'Learnit_Index_page'))
        # try:
        review = myReview.objects.create(Name=Name, Email=Email, Nationality = Nationality, Body = Body)
        review.save()
        messages.success(request, 'Thanks for reviewing us')
        return render(request, 'Learnit/index.html')
    
    if request.user.is_authenticated:
        student = Student.objects.get(user=user)
        fetch_review = myReview.objects.all()
        context = {'Review': fetch_review, "student": student, "user":user}
        # return redirect(reverse(request, 'Learnit_Index_page'))
        return render(request, 'Learnit/index.html', context) #USING THIS REQUIRES APP NAME
    return render(request, 'Learnit/index.html')

def Courses(request):
    return render(request, 'Learnit/courses.html')

def Contact(request):
    return render(request, 'Learnit/contact.html')

def About(request):
    return render(request, 'Learnit/about.html')

def Reviews(request):
    if request.method == 'POST':
        form = request.POST
        Name = form.get('Name')
        Email = form.get('Email')
        Nationality = form.get('Nationality')
        Body = form.get('Body')
        
        
        # if not Name or not Nationality or not Body or not Email:
        #     messages.error(request, "There is imcomplete field(s)")
        #     return redirect(reverse(request, 'Learnit_Index_page'))
        # try:
        review = myReview.objects.create(Name=Name, Email=Email, Nationality = Nationality, Body = Body)
        review.save()
        messages.success(request, 'Thanks for reviewing us')
        return redirect(reverse(request, 'Learnit_Index_page')) #USING THIS REQUIRES APP NAME
        # except:
        #     not Name or not Nationality or not Body or not Email 
        #     messages.error(request, "There is imcomplete field(s)")
        #     return redirect(reverse(request, 'Learnit_Index_page'))

    return render(request, 'Learnit/index.html')