from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.mail import send_mail
from django.db.models import Sum


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("afterlogin")
    return render(request,"greet/index.html")