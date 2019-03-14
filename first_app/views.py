from django.shortcuts import render
from django.http import HttpResponse
from .forms import newUser
from .emailsender import msg
# Create your views here.

def index(request):

    form = newUser()

    if request.method == 'POST':
        form = newUser(request.POST)

        if form.is_valid():
                form.save(commit=True)
                a = msg()
                a.sendemail(form.cleaned_data['email'],form.cleaned_data['first_name'])
                return thanks(request)
    
    return render(request,"first_app/index.html",{"form":form})
    

def thanks(request):
        return render(request,"first_app/thanks.html")