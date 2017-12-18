from __future__ import unicode_literals
from django.db import models
import bcrypt
import re 

NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        
        if len(self.filter(username=post_data['username'])) > 0:
            
            user = self.filter(username=post_data['username'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('username/password incorrect')
        else:
            errors.append('username/password incorrect')

        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        if len(post_data['name']) < 3 or len(post_data['username']) < 3:
            errors.append("Name and Username should be at least 3 characters")
        
        if len(post_data['password']) < 8:
            errors.append("Password must be at least 8 characters")
                   
        if not re.match(NAME_REGEX, post_data['name']):
            errors.append('Name fields must be letter characters only')
        
        if len(User.objects.filter(username=post_data['username'])) > 0:
            errors.append("There is another user with this username")
        
        if post_data['password'] != post_data['password_confirmation']:
            errors.append("Passwords do not match")

        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name=post_data['name'],
                username=post_data['username'],
                password=hashed
            )
            return new_user
        return errors

 

class User(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    objects=UserManager()
    def __str__(self):
        return self.username
    
# Create your models here.
