from django.shortcuts import render,redirect,reverse
from . import forms,models
from .models import Student, myCourse
from .forms import StudentForm
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from . import models as QMODEL
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from .forms import EditUserProfileForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# from django import forms
# from teacher import models as TMODEL


#for showing signup/login button for student
def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

@login_required(login_url='studentlogin')
@user_passes_test(is_student)


def student_signup(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    # studentForm=UserCreationForm ()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            return redirect(reverse('student:studentlogin')) #USING THIS REQUIRES APP NAME
        # return HttpResponseRedirect('studentlogin') #USING THIS DOES'NT REQUIRE APP NAME
    return render(request,'student/studentsignup.html',context=mydict)



def studentSignup(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    # studentForm=UserCreationForm ()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            return redirect(reverse('student:studentlogin')) #USING THIS REQUIRES APP NAME
        # return HttpResponseRedirect('studentlogin') #USING THIS DOES'NT REQUIRE APP NAME
    return render(request,'student/studentsignup.html',context=mydict)
    

def dashboard(request):
    user = request.user
    if request.method == "POST":
        return render(request,'student/for_dashboard.html')
    if request.user.is_authenticated:
        student_exit = Student.objects.filter(user=user).exists()
        if student_exit:
            student = Student.objects.get(user=user)
            context= {"student":student, "user":user }
        else:
            context= { "user":user }
        return render(request,'student/for_dashboard.html', context)
    else:    
        messages.info(request, "You are not authorized, kindly login")
        # return redirect(reverse('student:studentlogin'))
    return render(request,'student/for_dashboard.html')
    # return render(request,'student/for_dashboard.html', context)

def changeprofile(request):
    user = request.user
    if not request.user.is_authenticated:
        return redirect(reverse('student:studentlogin'))
    
    student_exit = Student.objects.filter(user=user).exists()
    if not student_exit:
        messages.error(request, 'There is no match for this username')
        return redirect(reverse('student:cahnge-profile')) #USING THIS REQUIRES APP NAME
    
    student = Student.objects.get(user=user)
    context = {'student':student, 'user': user}
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        first_name = form.get('first_name')
        last_name = form.get('last_name')
        mobile = form.get('mobile')
        address = form.get('address')
        email = form.get('email')
        img = request.FILES.get('profile_pic')
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.save()
        student.mobile = mobile
        student.email = email
        
        student.address = address
        if img:
            student.profile_pic = img
        student.save()
        messages.success(request, 'Your profile is updated successfully') 
        return redirect(reverse('student:student-dashboard')) #USING THIS REQUIRES APP NAME
        # return HttpResponseRedirect('student-dashboard') #USING THIS DOES'NT REQUIRE APP NAME
    return render(request, 'student/change_profile.html',context )



def Login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)                           
				messages.info(request, f"You are now logged in as {username}.")                              
				return redirect(reverse('student:student-dashboard')) #USING THIS REQUIRES APP NAME
				# return HttpResponseRedirect('student-dashboard') #USING THIS DOES'NT REQUIRE APP NAME
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="student/studentlogin.html", context={"login_form":forms})



def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("student:studentlogin")


def ForgotPassord(request):
    if request.method == "POST":
        form = request.POST
        email = form.get('email')
        student_exit = Student.objects.filter(email=email).exists()
        if not student_exit:
            messages.error(request, 'There is no record for this email')
        
    return render(request, 'student/forgotpassword.html')

def Course(request):
    user = request.user
    if request.method == 'POST':
        form = request.POST
        # return render(request, 'student/courseReg.html')
        if request.user.is_authenticated: 
            student_exit = Student.objects.filter(user=user).exists()
            if student_exit:
                my_student = Student.objects.get(user=user)
                # course_names = request.POST.getlist('course_names')
                course6 = form.get('WebDevelopment')
                course7 = form.get('PythonDevelopment')
                course8 = form.get('DevopTools')
                course9 = form.get('DataAnalysis')
                course10 = form.get('ML')
                course11 = form.get('Cloudcomp')
                course12 = form.get('ProjectManagement')
                course13 = form.get('CyberSecurity')
                course14 = form.get('BlockchainDevelopment')
                course15 = form.get('DigitalMarketing')
                course16 = form.get('UI_UXDesign')
                course17 = form.get('NLP')
                course18 = form.get('MobileDevelopment')
                course19 = form.get('IoT')
                
                if course6:
                    course=myCourse.objects.get(id=6)
                    my_student.studentcourse.add(course)
                if course7:
                    course=myCourse.objects.get(id=7)
                    my_student.studentcourse.add(course)
                if course8:
                    course=myCourse.objects.get(id=8)
                    my_student.studentcourse.add(course)
                if course9:
                    course=myCourse.objects.get(id=9)
                    my_student.studentcourse.add(course)
                if course10:
                    course=myCourse.objects.get(id=10)
                    my_student.studentcourse.add(course)
                if course11:
                    course=myCourse.objects.get(id=11)
                    my_student.studentcourse.add(course)
                if course12:
                    course=myCourse.objects.get(id=12)
                    my_student.studentcourse.add(course)
                if course13:
                    course=myCourse.objects.get(id=13)
                    my_student.studentcourse.add(course)
                if course14:
                    course=myCourse.objects.get(id=14)
                    my_student.studentcourse.add(course)
                if course15:
                    course=myCourse.objects.get(id=15)
                    my_student.studentcourse.add(course)
                if course16:
                    course=myCourse.objects.get(id=16)
                    my_student.studentcourse.add(course)
                if course17:
                    course=myCourse.objects.get(id=17)
                    my_student.studentcourse.add(course)
                if course18:
                    course=myCourse.objects.get(id=18)
                    my_student.studentcourse.add(course)
                if course19:
                    course=myCourse.objects.get(id=19)
                    my_student.studentcourse.add(course)
                                        
                my_student.save()
                studentCourse = Student.studentcourse
                print(studentCourse)
                messages.success(request, 'Courses selected',{'studentCourse':studentCourse})
                return redirect(reverse('student:payment')) #USING THIS REQUIRES APP NAME
        #     stdId = currentStudent.id
            else:
                messages.error(request, 'The authenticated user does not exist in the category of STUDENT, kindly login first')
                return render(request, 'student/courseReg.html')
        else:
            messages.error(request, 'This user is not authenticated')
            return render(request, 'student/courseReg.html')    
    return render(request, 'student/courseReg.html')
        


def buyCourse(request):
    return render(request, 'student/payment.html')
        
        