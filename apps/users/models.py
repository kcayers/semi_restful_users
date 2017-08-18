from __future__ import unicode_literals

from django.db import models

import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z]+$')
        errors = {}
        for value in postData.itervalues():
            if value == '':
                errors["empty_fields"] = "All fields must be completed"
        if not postData['first_name'].isalpha() or not postData['last_name'].isalpha():
    		errors["letters_only"] = "First and Last Name must be letters only"
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors["name"] = "First and last names should be longer than one letter"
        if not EMAIL_REGEX.match(postData['email']):
    		errors["email"] = "Invalid email address"
        query = User.objects.filter(email=postData['email'])
        if len(query) != 0:
            errors["already_exitst"] = "Email already exits"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
