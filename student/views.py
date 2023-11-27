from django.shortcuts import render,redirect,reverse
from . import forms,models
from .models import Student, myCourse, Proof
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User
import re


def validate_password(password):
    # Define regular expression patterns for required characters
    required_char_patterns = {
        'uppercase': r'[A-Z]',
        'lowercase': r'[a-z]',
        # 'digit': r'[0-9]',
        'special': r'[!@#$%^&*()_+-]'
    }

    # Check if the password contains all required characters
    for char_type, pattern in required_char_patterns.items():
        if not re.search(pattern, password):
            return False

    # If all required characters are present, return True
    return True

def studentSignup(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    # studentForm=UserCreationForm ()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        if len(username) < 8:
            messages.error(request, 'Username must be a minimum of 8 character')
            return render(request,'student/studentsignup.html',context=mydict)
        username_exit = User.objects.filter(username=username).exists()
        if username_exit:
            messages.error(request, 'Username already taken')
            return render(request,'student/studentsignup.html',context=mydict)
        email_exit = User.objects.filter(email=email).exists()
        if email_exit:
            messages.error(request, 'email provided already in use')
            return render(request,'student/studentsignup.html',context=mydict)
        if username == password:
            messages.error(request, 'email and password can not be the same')
            return render(request,'student/studentsignup.html',context=mydict)
        if not validate_password(password):
            # Display an error message if the password is invalid
            messages.error(request, 'Password must contain at least one uppercase letter, one lowercase letter and one special character.')
            return render(request,'student/studentsignup.html',context=mydict)
        if not userForm.is_valid() and not studentForm.is_valid():
            messages.error(request, 'Your details are not valid')
            return render(request,'student/studentsignup.html',context=mydict)
        user=userForm.save()
        user.set_password(user.password)
        user.save()
        student=studentForm.save(commit=False)
        student.user=user
        student.save()
        my_student_group = Group.objects.get_or_create(name='STUDENT')
        my_student_group[0].user_set.add(user)
        return redirect(reverse('student:studentlogin')) #USING THIS REQUIRES APP NAME
    return render(request,'student/studentsignup.html',context=mydict)
    
'''
def dashboard(request):    
    if request.method == "POST":
        user = request.user
        return render(request,'student/for_dashboard.html')
    if request.user.is_authenticated:
        student_exit = Student.objects.filter(user=user).exists()
        if student_exit:
            # my_student = Student.objects.get(user=user)
            student = Student.objects.get(user=user)
            studentCourse = student.studentcourse.all()
            context= {"student":student, "user":user,'studentCourse':studentCourse}
        else:
            context= { "user":user }
        return render(request,'student/for_dashboard.html', context)
    else:    
        messages.info(request, "You are not authorized, kindly login")
    return render(request,'student/for_dashboard.html')
'''
def studentDashboard(request):    
    user = request.user
    if request.method == "POST":
        return render(request,'student/for_dashboard.html')
    if request.user.is_authenticated:
        student_exit = Student.objects.filter(user=user).exists()
        if student_exit:
            # my_student = Student.objects.get(user=user)
            student = Student.objects.get(user=user)
            studentCourse = student.studentcourse.all()
            context= {"student":student, "user":user,'studentCourse':studentCourse}
        else:
            context= { "user":user }
        return render(request,'student/for_dashboard.html', context)
    else:    
        messages.info(request, "You are not authorized, kindly login")
    return render(request,'student/for_dashboard.html')

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
    courses = myCourse.objects.all()
    context = {"courses":courses}
    
    if request.method == 'POST':
        form = request.POST
        if request.user.is_authenticated: 
            student_exit = Student.objects.filter(user=user).exists()
            if student_exit:
                my_student = Student.objects.get(user=user)
                for p in form:
                    if p != 'csrfmiddlewaretoken':
                        try:
                            id = int(p)
                            course=myCourse.objects.get(id=id)
                            my_student.studentcourse.add(course)
                            
                        except BaseException:
                            pass
                my_student.save()
                studentCourse = my_student.studentcourse.all()
                courses = ""
                for idx, course in enumerate(studentCourse):
                    if idx == 0:
                        courses = course.coursename
                    elif idx == len(studentCourse) - 1:
                        courses = courses + " " + course.coursename
                    else:
                        courses = courses + " " + course.coursename + ","
                # messages.success(request, f'Courses selected:{courses}')
                return redirect(reverse('student:payment')) #USING THIS REQUIRES APP NAME
            else:
                messages.error(request, 'The authenticated user does not exist in the category of STUDENT, kindly login first')
                return render(request, 'student/courseReg.html')
        else:
            messages.error(request, 'This user is not authenticated')
            return render(request, 'student/courseReg.html')    
    return render(request, 'student/courseReg.html', context)
        


def buyCourse(request):
    user = request.user
    my_student = Student.objects.get(user=user)
    studentCourse = my_student.studentcourse.all()
    
    if request.method == 'POST':
        form = request.POST
        if request.user.is_authenticated: 
            student_exit = Student.objects.filter(user=user).exists()
            if student_exit:                                
                receipt = request.FILES.get('receipt')
                student = request.user.student
                if receipt or student:
                    paymentProof =  Proof.objects.create(receipt=receipt, student=student)
                    paymentProof.save()
                    messages.success(request, "Your proof of payment has been uploaded")
                    return redirect(reverse('student:student-dashboard')) #USING THIS REQUIRES APP NAME
                else:
                    student = None
                    messages.error(request, "You must upload a payment proof")
                    return render(request, 'student/payment.html')
            else:
                messages.error(request, 'The authenticated user does not exist in the category of STUDENT, kindly login first')
                return render(request, 'student/payment.html')
        else:
            messages.error(request, 'This user is not authenticated')
            return render(request, 'student/payment.html')      
                
    return render(request, 'student/payment.html', {'studentCourse':studentCourse})

        
        