from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
from . import forms

# Create your views here.
def index(request):
    data = {"data":User.objects.order_by("first_name")}
    return render(request,"user/user_page.html",context=data)

def formrequest(request):
    formname = forms.Userform()
    return render(request,"user/user_form.html",{"form":formname})