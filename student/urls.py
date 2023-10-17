from django.urls import path
from student import views
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView

app_name = 'student' 


urlpatterns = [
path('studentclick', views.studentclick_view),
# path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
path('studentlogin', views.Login,name='studentlogin'),
path("logout", views.logout_request, name= "logout"),
path('changepassword', PasswordResetView.as_view(template_name='student/forgotpassword.html'),name='changepassword'),
path('resetdone', PasswordResetDoneView.as_view(template_name='student/resetdone.html'),name='resetdone'),
path('resetcomplete', PasswordResetCompleteView.as_view(template_name='student/resetcomplete.html'),name='resetcomplete'),
path('resetconfirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='student/resetconfirm.html'),name='resetconfirm'),
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
path('studentsignup', views.student_signup_view,name='studentsignup'),
path('student-dashboard', views.dashboard,name='student-dashboard'),
path('student/<str:id>', views.eachstudent,name='student'),

# path('student-exam', views.student_exam_view,name='student-exam'),
# path('take-exam/<int:pk>', views.take_exam_view,name='take-exam'),
# path('start-exam/<int:pk>', views.start_exam_view,name='start-exam'),

# path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
# path('view-result', views.view_result_view,name='view-result'),
# path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
# path('student-marks', views.student_marks_view,name='student-marks'),
]