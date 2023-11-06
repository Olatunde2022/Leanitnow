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



# def studentclick_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect('afterlogin')
#     return render(request,'student/studentclick.html')

# def is_student(user):
#     return user.groups.filter(name='STUDENT').exists()

# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)


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
    my_student = Student.objects.get(user=user)
    studentCourse = my_student.studentcourse.all()
    if request.method == "POST":
        return render(request,'student/for_dashboard.html')
    if request.user.is_authenticated:
        student_exit = Student.objects.filter(user=user).exists()
        if student_exit:
            student = Student.objects.get(user=user)
            context= {"student":student, "user":user,'studentCourse':studentCourse}
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
    courses = myCourse.objects.all()
    context = {"courses":courses}
    
    if request.method == 'POST':
        form = request.POST
        # return render(request, 'student/courseReg.html')
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
                messages.success(request, f'Courses selected:{courses}')
                return redirect(reverse('student:payment')) #USING THIS REQUIRES APP NAME
        #     stdId = currentStudent.id
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
                # my_student = Student.objects.get(user=user)
                                
                receipt = request.FILES.get('receipt')
                if receipt:
                    paymentProof =  Proof.objects.create(receipt=receipt)
                    paymentProof.save()
                    messages.success(request, "Your proof of payment has been uploaded")
                    return redirect(reverse('student:student-dashboard')) #USING THIS REQUIRES APP NAME
                else:
                    messages.error(request, "You must upload a payment proof")
                    return render(request, 'student/payment.html')
            else:
                messages.error(request, 'The authenticated user does not exist in the category of STUDENT, kindly login first')
                return render(request, 'student/payment.html')
        else:
            messages.error(request, 'This user is not authenticated')
            return render(request, 'student/payment.html')      
                
    return render(request, 'student/payment.html', {'studentCourse':studentCourse})

        
        