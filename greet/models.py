from django.db import models
from django.contrib.auth.models import User

classes=[('one','one'),('two','two'),('three','three'),('four','four'),('five','five'),('six','six'),
         ('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll=models.CharField(max_length=10)
    mobile=models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl=models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" " + self.user.last_name
    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

# Create your models here.
class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary=models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile=models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='greet')
    message=models.CharField(max_length=500)

class Attendance(models.Model):
    role=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status=models.CharField(max_length=10)