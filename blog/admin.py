from django.contrib import admin

from .models import Blog
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import NewUser

# admin.site.register(NewUser, UserAdmin)

admin.site.register(Blog)