"""
URL configuration for myinstitute project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [   
    path('', views.Index, name='Learnit_Index_page'),
    path('courses/', views.Courses, name='Learnit_Courses_page'),
    path('contact/', views.Contact, name='Learnit_Contact_page'),
    path('about/', views.About, name='Learnit_About_page'),
]
