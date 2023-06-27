from django.db import models
from django.contrib.auth.models import User

classes=[('one','one'),('two','two'),('three','three'),('four','four'),('five','five'),('six','six'),
         ('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=10)
    mobile=models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl=models.CharField(max_length=10,choices=classes,default='one')
    status=models.BooleanField(default=False)
    @@property
    def get_name(self):
        return self.user.first_name+" " + self.user.last_name
    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

# Create your models here.
