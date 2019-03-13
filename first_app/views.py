from django.shortcuts import render
from django.http import HttpResponse
from .forms import newUser
# Create your views here.

def index(request):

    form = newUser()

    if request.method == 'POST':
        form = newUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    
    return render(request,"first_app/index.html",{"form":form})
    

    