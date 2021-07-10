from django.contrib.auth import models
from rest_framework.serializers import ModelSerializer

from .models import RestBlog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = RestBlog
        fields = ['id', 'title', 'content', ]