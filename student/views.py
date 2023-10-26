from django.shortcuts import render,redirect,reverse
from . import forms,models
from .models import Student
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

# def student_dashboard_view(request,id):
#     # dict={
    
#     # 'total_course':QMODEL.Course.objects.all().count(),
#     # 'total_question':QMODEL.Question.objects.all().count(),
#     # }
#     each_student = Student.objects.get(id=id)
#     context= {"student":each_student}
    
#     return render(request,'student/for_dashboard.html', context)



# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# def student_exam_view(request):
#     courses=QMODEL.Course.objects.all()
#     return render(request,'student/student_exam.html',{'courses':courses})

# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# def take_exam_view(request,pk):
#     course=QMODEL.Course.objects.get(id=pk)
#     total_questions=QMODEL.Question.objects.all().filter(course=course).count()
#     questions=QMODEL.Question.objects.all().filter(course=course)
#     total_marks=0
#     for q in questions:
#         total_marks=total_marks + q.marks
    
#     return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})

# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# def start_exam_view(request,pk):
#     course=QMODEL.Course.objects.get(id=pk)
#     questions=QMODEL.Question.objects.all().filter(course=course)
#     if request.method=='POST':
#         pass
#     response= render(request,'student/start_exam.html',{'course':course,'questions':questions})
#     response.set_cookie('course_id',course.id)
#     return response


# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# def calculate_marks_view(request):
#     if request.COOKIES.get('course_id') is not None:
#         course_id = request.COOKIES.get('course_id')
#         course=QMODEL.Course.objects.get(id=course_id)
        
#         total_marks=0
#         questions=QMODEL.Question.objects.all().filter(course=course)
#         for i in range(len(questions)):
            
#             selected_ans = request.COOKIES.get(str(i+1))
#             actual_answer = questions[i].answer
#             if selected_ans == actual_answer:
#                 total_marks = total_marks + questions[i].marks
#         student = models.Student.objects.get(user_id=request.user.id)
#         result = QMODEL.Result()
#         result.marks=total_marks
#         result.exam=course
#         result.student=student
#         result.save()

#         return HttpResponseRedirect('view-result')



# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# def view_result_view(request):
#     courses=QMODEL.Course.objects.all()
#     return render(request,'student/view_result.html',{'courses':courses})
    

# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# def check_marks_view(request,pk):
#     course=QMODEL.Course.objects.get(id=pk)
#     student = models.Student.objects.get(user_id=request.user.id)
#     results= QMODEL.Result.objects.all().filter(exam=course).filter(student=student)
#     return render(request,'student/check_marks.html',{'results':results})

# @login_required(login_url='studentlogin')
# @user_passes_test(is_student)
# def student_marks_view(request):
#     courses=QMODEL.Course.objects.all()
#     return render(request,'student/student_marks.html',{'courses':courses})



# def login_user(request):
#     next = ""

#     if request.GET:  
#         next = request.GET['next']

#     if request.POST:
#         username = request.POST['username']
#         password = request.POST['password']

#     def is_student(user):
#         return user.groups.filter(name='STUDENT').exists()
#         # user = authenticate...
#         # login(request, user)
#     if next == "":
#         return render(request,'student/studentlogin.html')
#     else:
#             return HttpResponseRedirect(next)
        

# class UpdateUserView(generic.UpdateView):
#     form_class = EditUserProfileForm
#     template_name = "student/change_profile.html"
#     success_url = reverse_lazy('student:student-dashboard')
    
    
#     def get_object(self):
#         return self.request.user
#     # def get_object(self):
#     #     return self.request.Student
    


# def Login(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     # return  render(request, 'student/studentlogin.html')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponseRedirect('student-dashboard')
#         # Redirect to a success page.
#         ...
#     else:
#         # Return an 'invalid login' error message.
#         return  HttpResponse('<h3>There is an error from login request</h3>')

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    # studentForm=UserCreationForm ()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        # if userForm and studentForm != None:
        #     messages.success(request, "You've successfully signup with us")
        #     return redirect(reverse('studentlogin'))
        # else:
        #     messages.error(request,'There is empty field, kindly check')
        #     return render(request,'student/studentsignup.html',context=mydict)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('studentlogin') #USING THIS DOES'NT REQUIRE APP NAME
    return render(request,'student/studentsignup.html',context=mydict)


def dashboard(request):
    user = request.user
    if request.method == "POST":
        return render(request,'student/for_dashboard.html')
    if request.user.is_authenticated:
        student = Student.objects.get(user=user)
        context= {"student":student, "user":user }
        return redirect(reverse('student-dashboard', context))#USING THIS REQUIRES APP NAME
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
        return HttpResponseRedirect('student-dashboard') #USING THIS DOES'NT REQUIRE APP NAME
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
				return HttpResponseRedirect('student-dashboard') #USING THIS DOES'NT REQUIRE APP NAME
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

