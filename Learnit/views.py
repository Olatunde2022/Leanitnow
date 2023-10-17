from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'Learnit/index.html')

def Courses(request):
    return render(request, 'Learnit/courses.html')

def Contact(request):
    return render(request, 'Learnit/contact.html')

def About(request):
    return render(request, 'Learnit/about.html')
