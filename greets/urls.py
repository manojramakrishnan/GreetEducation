"""greets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from greet import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('adminclick',views.adminclick_view),
    path('teacherclick',views.teacherclick_view),
    path('studentclick',views.studentclick_view),
    path('aboutus',views.aboutus_view),
    path('contactus',views.contactus_view),
    path('studentsignup',views.studentsignup_view),
    path('adminsignup',views.admin_signup_view),
    path('adminlogin',LoginView.as_view(template_name='greet/adminlogin.html')),
    path('teachersignup',views.teacher_signup_view),
    path('teacherlogin',LoginView.as_view(template_name='greet/teacherlogin.html')),
    path('studentsignup',views.student_signup_view),
    path('studentlogin',LoginView.as_view(template_name='greet/studentlogin.html')),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('admin-dashboard',views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-teacher',views.admin_teacher_view,name='admin-teacher'),
    path('admin-student',views.admin_student_view,name='admin-student')

]
