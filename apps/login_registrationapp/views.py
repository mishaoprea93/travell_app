from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request,'login_registrationapp/index.html')

def register_login(request):
    if request.method=="POST":
        if request.POST['action']=="register":           
            result = User.objects.validate_registration(request.POST)
            if type(result) == list:
                for err in result:
                    messages.error(request, err)
                return redirect('/main')
            request.session['user_id'] = result.id
            messages.success(request, "Successfully registered!")
            return redirect('/travels')
        
        if request.POST['action']=="login":                        
            result = User.objects.validate_login(request.POST)
            if type(result) == list:
                for err in result:
                    messages.error(request, err)
                return redirect('/main')
            request.session['user_id'] = result.id
            messages.success(request, "Successfully logged in!")
            return redirect('/travels')

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/main')
 