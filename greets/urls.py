from django.contrib import admin
from django.urls import path
from greet import views
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home_view,name=''),
    path('adminclick',views.adminclick_views),
    path('teacherclick',views.teacherclick_views),
    path('studentclick',views.studentclick_views),
    path('adminsignup',views.admin_signup_views),
    path('teachersignup',views.teacher_signup_views),
    path('studentsignup',views.student_signup_views),
    path('adminlogin',LoginView.as_view(templates_name='greet/adminlogin.html')),
    path('teacherlogin',LoginView.as_view(templates_name='greet/teacherlogin.html')),
    path('studentlogin',LoginView.as_view(templates_name='greet/studentlogin.html')),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('logout',LogoutView.as_view(template_name='greet/index.html'),name='logout'),
    path('admin-dashboard',views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-teacher',views.admin_teacher_view,name='admin-teacher'),
    path('admin-add-teacher',views.admin_add_teacher_view,name='admin-add-teacher'),
    path('admin-view-teacher',views.admin_view_teacher_view,name='admin-view-teacher'),
    path('admin-approve-teacher',views.admin_approve_teacher_view,name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>',views.approve_teacher_view,name='approve-teacher'),
    path('delete-teacher/<int:pk>',views.delete_teacher_view,name='delete-teacher'),
    path('delete-teacher-from-school/<int:pk>',views.delete_teacher_from_school_view,name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>',views.update_teacher_view,name='update-teacher'),
    path('admin-view-teacher-salary',views.admin_view_teacher_salary_view,name='admin-view-teacher-salary'),



    path('admin-student',views.admin_student_view,name='admin-student'),
    path('admin-add-student',views.admin_add_student_view,name='admin-add-student'),
    path('admin-view-student',views.admin_view_student_view,name='admin-view-student'),
    path('delete-student/<int:pk>',views.delete_student_view,name='delete-student'),
    path('delete-student-from-school/<int:pk>',views.delete_student_from_school_view,name='delete-student-from-school'),
    path('admin-approve-student',views.admin_approve_student_view,name='admin-approve-student'),
    path('approve-student/<int:pk>',views.approve_student_view,name='approve-student'),
    path('admin-view-student-fee',views.admin_view_student_fee_view,name='admin-view-student-fee'),
    path('update-student/<int:pk>',views.update_student_view,name='update-student'),



    path('admin-attendence',views.admin_attendence_view,name='admin-attendence'),
    path('admin-take-attendence/<str:cl>',views.admin_take_attendence_view,name='admin-take-attendence'),
    path('admin-view-attendence/<str:cl>',views.admin_view_attendence_view,name='admin-view-attendence'),
    path('admin-view-fee/<str:cl>',views.admin_view_fee_view,name='admin-view-fee'),
    path('admin-notice',views.admin_notice_view,name='admin-notice'),
    path('teacher-dashboard',views.teacher_dashboard_view,name='teacher-dashboard'),
    path('teacher-attendence',views.teacher_attendence_view,name='teacher-attendence'),
    path('teacher-take-attendence/<str:cl>',views.teacher_take_attendence_view,name='teacher-take-attendence'),
    path('teacher-view-attendence/<str:cl>',views.teacher_view_attendence_view,name='teacher-view-attendence'),
    path('teacher-notice',views.teacher_notice_view,name='teacher-notice'),
    path('student-dashboard', views.student_dashboard_view, name='student-dashboard'),
    path('student-attendence', views.student_attendence_view, name='student-attendence'),


    path('aboutus',views.adboutus_view),
    path('contactus',views.contactus_view)
]