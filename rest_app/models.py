from django.db import models
from django.db.models.base import Model


class RestBlog(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    
