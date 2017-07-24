from __future__ import unicode_literals
import uuid
from django.db import models

import uuid

class UserModel(models.Model):
    name            = models.CharField(max_length=120, null=False)
    email           = models.EmailField()
    username        = models.CharField(max_length=120, unique=True)
    password        = models.CharField(max_length=40)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)



class SessionToken(models.Model):
    user            = models.ForeignKey(UserModel)
    session_token   = models.CharField(max_length=120)
    created_on      = models.DateTimeField(auto_now_add=True)
    is_valid        = models.BooleanField(default=True)

    def create_token(self):
        self.session_token = uuid.uuid4()

    def delete(self):
        d = self.user.id
        SessionToken.objects.get(id__exact=d).delete()
        # self.user.id = None
        self.is_valid = False
        self.session_token = ''

class PostModel(models.Model):
    user            = models.ForeignKey(UserModel)
    image           = models.FileField(upload_to='user_images')
    image_url       = models.CharField(max_length=255)
    caption         = models.CharField(max_length=240)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)
    tags            = models.TextField(null=True)
    has_liked       = False

    @property
    def like_count(self):
        return len(LikeModel.objects.filter(post=self))

    @property
    def comments(self):
        return CommentModel.objects.filter(post=self).order_by('created_on')

class LikeModel(models.Model):
    user            = models.ForeignKey(UserModel)
    post            = models.ForeignKey(PostModel)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)

class CommentModel(models.Model):
    user            = models.ForeignKey(UserModel)
    post            = models.ForeignKey(PostModel)
    # likes         = models.ForeignKey(LikeModel)
    comment_text    = models.CharField(max_length=555)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)
    has_upvoted     = False

    @property
    def upvote_count(self):
        return len(UpvoteModel.objects.filter(comment=self))

class UpvoteModel(models.Model):
    user            = models.ForeignKey(UserModel)
    comment         = models.ForeignKey(CommentModel)
    created_on      = models.DateTimeField(auto_now_add=True)
    updated_on      = models.DateTimeField(auto_now=True)
