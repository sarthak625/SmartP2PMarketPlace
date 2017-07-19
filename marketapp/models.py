from __future__ import unicode_literals

from django.db import models

class UserModel(models.Model):
    name    = models.CharField(max_length=120, null=False)
    email       = models.EmailField()
    username    = models.CharField(max_length=120, unique=True)
    password    = models.CharField(max_length=40)
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on  = models.DateTimeField(auto_now=True)

class SessionToken(models.Model):
    user            = models.ForeignKey(UserModel)
    session_token   = models.CharField(max_length=120)
    created_on      = models.DateTimeField(auto_now_add=True)
    is_valid        = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()
