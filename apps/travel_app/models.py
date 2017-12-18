from __future__ import unicode_literals
from ..login_registrationapp.models import User
from django.db import models
from datetime import date


class TravelManager(models.Manager):
    def validate_travels(self,post_data):
        errors = []
        if len(post_data['destination']) < 1 or len(post_data['description']) < 1:
            errors.append("Destination and Description can not be empty fields")
        if len(post_data['date_from']) < 1 or len(post_data['date_to']) < 1:
            errors.append("Dates can not be empty fields")
        # if date.time.now()>post_data['date_from']:
        #     errors.append("From date can not be in the past")
        # if post_data['date_to']<post_data['date_from']:
        #     errors.append("Select a date after the Start From")
        
        return errors     


class Trip(models.Model):
    destination=models.CharField(max_length=255)
    description=models.TextField()
    date_from=models.DateField(default=date.today)
    date_to=models.DateField(default=date.today)
    user=models.ForeignKey(User,related_name="created_by")
    joiners=models.ManyToManyField(User,related_name="joined_by")
    objects=TravelManager()
    def __str__(self):
        return self.destination