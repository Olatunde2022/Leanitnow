from django.urls import path
from django.contrib.auth import views as auth_views
from student import views
from django.contrib.auth.views import LoginView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static
app_name = 'student' 


urlpatterns = [
path('studentclick', views.studentclick_view),
# path('studentlogin', LoginView.as_view(template_name='student/studentlogin.html'),name='studentlogin'),
path('studentlogin', views.Login,name='studentlogin'),
path("logout", views.logout_request, name= "logout"),
# path('resetdone', PasswordResetDoneView.as_view(template_name='student/resetdone.html'),name='resetdone'),
# path('resetcomplete', PasswordResetCompleteView.as_view(template_name='student/resetcomplete.html'),name='resetcomplete'),
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
path('studentsignup', views.studentSignup,name='studentsignup'),
path('student-dashboard', views.dashboard,name='student-dashboard'),
path('course-reg', views.Course,name='course-reg'),
path('payment', views.buyCourse,name='payment'),
path('cahnge-profile', views.changeprofile,name='cahnge-profile'),
path('pssword-reset', auth_views.PasswordResetView.as_view(template_name='student/forgotpassword.html'),name='pssword_reset'),
path('resetdone', auth_views.PasswordResetDoneView.as_view(template_name='student/resetdone.html'),name='resetdone'),
path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='student/resetconfirm.html'),name='password_reset_confirm'),
# path('changepassword', views.ForgotPassord,name='changepassword'),
]

# urlpatterns+= static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)