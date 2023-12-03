from django.urls import path
from django.contrib.auth import views as auth_views
from student import views
app_name = 'student' 


urlpatterns = [
path('studentsignup', views.studentSignup,name='studentsignup'),
path('studentlogin', views.Login,name='studentlogin'),
# path('password-reset/', views.password_reset, name='password_reset'),
# path('password-reset-confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
path('student-dashboard', views.studentDashboard,name='student-dashboard'),
path('cahnge-profile', views.changeprofile,name='cahnge-profile'),
path("logout", views.logout_request, name= "logout"),
path('course-reg', views.Course,name='course-reg'),
path('payment', views.buyCourse,name='payment'),
]