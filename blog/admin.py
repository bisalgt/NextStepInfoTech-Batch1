from django.contrib import admin

from .models import Blog, NewUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


admin.site.register(Blog)
admin.site.register(NewUser)