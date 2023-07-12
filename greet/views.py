from django.shortcuts import render,redirect,reverse
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from . import forms,models
from django.core.mail import send_mail


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'greet/index.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'greet/adminclick.html')

def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'greet/teacherclick.html')

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'greet/studentclick.html')

def aboutus_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'greet/aboutus.html')

def contactus_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'greet/contactus.html')

def studentsignup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'greet/studentsignup.html')

def admin_signup_view(request):
    form= forms.AdminSignupForm()
    if request.method=='POST':
        form=forms.AdminSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group=Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            return HttpResponseRedirect('adminlogin')
    return render(request,'greet/adminsignup.html',{'form':form})

def teacher_signup_view(request):
    form1= forms.TeacherUserForm()
    form2=forms.TeacherExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.TeacherUserForm(request.POST)
        form2 = forms.TeacherExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()
            my_teacher_group=Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)
            return HttpResponseRedirect('teacherlogin')
    return render(request,'greet/teachersignup.html',context=mydict)

def student_signup_view(request):
    form1= forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.StudentUserForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()

            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
            f2.user=user
            user2=f2.save()
            my_student_group=Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            return HttpResponseRedirect('studentlogin')
    return render(request,'greet/studentsignup.html',context=mydict)

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_teacher(request.user):
        accountapprovable=models.TeacherExtra.objects.all().filter(user_id=request.user.id,status=True)
        if accountapprovable:
            return redirect('teacher-dashboard')
        else:
            return render(request,'greet/teacher_wait_for_approval.html')
    elif is_student(request.user):
        accountapprovable=models.StudentExtra.objects.all().filter(user_id=request.user.id,status=True)
        if accountapprovable:
            return redirect('student-dashboard')
        else:
            return render(request,'greet/student_wait_for_approval.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    teachercount=models.TeacherExtra.objects.all().filter(status=True).count()
    pendingteachercount=models.TeacherExtra.objects.all().filter(status=False).count()
    studentcount = models.StudentExtra.objects.all().filter(status=True).count()
    pendingstudentcount = models.StudentExtra.objects.all().filter(status=False).count()
    teachersalary = models.TeacherExtra.objects.all().filter(status=True).aggregate(Sum('salary'))
    pendingteachersalary = models.TeacherExtra.objects.all().filter(status=False).aggregate(Sum('salary'))
    studentfee = models.StudentExtra.objects.all().filter(status=True).aggregate(Sum('fee',default=0))
    pendingstudentfee = models.StudentExtra.objects.all().filter(status=False).aggregate(Sum('fee'))
    notice=models.Notice.objects.all()


    mydict={
        'teachercount':teachercount,
        'pendingteachercount':pendingteachercount,
        'studentcount':studentcount,
        'pendingstudentcount':pendingstudentcount,
        'teachersalary':teachersalary['salary__sum'],
        'pendingteachersalary':pendingteachersalary['salary__sum'],
        'studentfee':studentfee['fee__sum'],
        'pendingstudentfee':pendingstudentfee['fee__sum'],
        'notice':notice
    }
    return render(request,'greet/admin_dashboard.html',context=mydict)

# Create your views here.

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_teacher_view(request):
    return render(request,'greet/admin_teacher.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_student_view(request):
    return render(request,'greet/admin_student.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_admin)
def admin_fee_view(request):
    return render(request,'greet/admin_fee.html')