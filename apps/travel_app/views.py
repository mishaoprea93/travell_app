from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from ..login_registrationapp.models import User
from .models import Trip
import datetime
from django.contrib import messages

def travels(request):
    others=Trip.objects.all().exclude(user=request.session['user_id'])
    context={
        "user":User.objects.get(id=request.session['user_id']),
        "trips":Trip.objects.filter(joiners=request.session['user_id']),
        "others":others  
    }
    return render(request,'travel_app/travels.html',context)


def add(request):
    return render(request,'travel_app/add.html')

def process_trip(request):
    errors = Trip.objects.validate_travels(request.POST)
    if len(errors)>0:
        for err in errors:
            messages.error(request, err)
        return redirect('/travels/add')
    else:
        user1=User.objects.get(id=request.session['user_id'])
        new_trip=Trip.objects.create(
                destination=request.POST['destination'],
                description=request.POST['description'],
                date_from=request.POST['date_from'],
                date_to=request.POST['date_to'],
                user=user1,
            )
        this_trip=Trip.objects.last()
        this_trip.joiners.add(user1)
        return redirect('/travels')

def join_trip(request,id):
    this_user=User.objects.get(id=request.session['user_id'])
    this_trip=Trip.objects.get(id=id)
    this_trip.joiners.add(this_user)
    return redirect('/travels')
    
def destination(request,id):
    this_trip=Trip.objects.get(id=id)
    userss=this_trip.joiners.all()
    context={
        "this_trips":this_trip,
        "userrs":userss
    }
    return render(request,'travel_app/destination.html',context)
