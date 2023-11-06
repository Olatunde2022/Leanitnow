from django.urls import path
from django.contrib.auth import views as auth_views
from student import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'student' 


urlpatterns = [
path('studentlogin', views.Login,name='studentlogin'),
path("logout", views.logout_request, name= "logout"),
path('studentsignup', views.studentSignup,name='studentsignup'),
path('student-dashboard', views.dashboard,name='student-dashboard'),
path('course-reg', views.Course,name='course-reg'),
path('payment', views.buyCourse,name='payment'),
path('cahnge-profile', views.changeprofile,name='cahnge-profile'),
]