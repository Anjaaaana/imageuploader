from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate
from subprocess import call

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username= username, password=password)
        if user is not None:
            messages.success(request, 'login successful')
            return render(request,'index.html')
        else:
            messages.warning(request, 'invalid username or password')
            return render(request,'login.html')
    return render(request,'login.html')




def index(request):
    return render(request, 'index.html')