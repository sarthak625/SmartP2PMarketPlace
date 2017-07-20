from django.contrib import admin
from models import UserModel, PostModel

# Registered models to view on /admin
admin.site.register(UserModel)
admin.site.register(PostModel)
