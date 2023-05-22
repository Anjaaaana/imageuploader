from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('C:\Users\Lenovo\Desktop\major project\vacancy-and-tender-extraction\v_and_t_extraction\imageuploader\myapp\migrations\image_uploader.py') # redirect to image uploader view
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')
