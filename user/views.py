from django.shortcuts import render
from django.http import HttpResponse
from user.models import User

# Create your views here.
def index(request):
    data = {"data":User.objects.order_by("first_name")}
    return render(request,"user/user_page.html",context=data)