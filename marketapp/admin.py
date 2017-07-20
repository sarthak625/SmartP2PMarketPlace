from django.contrib import admin
from models import *

# Registered models to view on /admin
admin.site.register(UserModel)
admin.site.register(PostModel)
admin.site.register(LikeModel)
