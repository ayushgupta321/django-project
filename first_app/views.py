from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    text_dict = {"text_here": "This is good"}
    return render(request,"first_app/index.html",context=text_dict)
    

    