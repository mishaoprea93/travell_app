from __future__ import unicode_literals
from ..login_registrationapp.models import User
from django.db import models
from datetime import datetime
from time import strptime,strftime

class TravelManager(models.Manager):
    def validate_travels(self,post_data):
        errors = []
        today=datetime.today()
        date_from1=strptime(post_data['date_from'],"%Y-%m-%d")
        date_from2=datetime(*date_from1[:3])
        print date_from2
        date_to1=strptime(post_data['date_to'],"%Y-%m-%d")
        date_to2=datetime(*date_to1[:3])
        print date_to2
        if len(post_data['destination']) < 1 or len(post_data['description']) < 1:
            errors.append("Destination and Description can not be empty fields")
        if len(post_data['date_from']) < 1 or len(post_data['date_to']) < 1:
            errors.append("Dates can not be empty fields")
        if today>date_from2:
            errors.append("You can not start your trip in the past!")
        if date_to2<date_from2:
            errors.append("Your trip can not end before it started.Please insert a valid date!")
        
        return errors     


class Trip(models.Model):
    destination=models.CharField(max_length=255)
    description=models.TextField()
    date_from=models.DateField(default=datetime.today)
    date_to=models.DateField(default=datetime.today)
    user=models.ForeignKey(User,related_name="created_by")
    joiners=models.ManyToManyField(User,related_name="joined_by")
    objects=TravelManager()
    def __str__(self):
        return self.destination