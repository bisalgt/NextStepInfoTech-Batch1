from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.enums import Choices
from django.urls import reverse

#Many blogs related to single author
class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug_field = models.SlugField(null=True, blank=True)
    author = models.ForeignKey('NewUser', on_delete=CASCADE, null=True, blank=True) # ManyToONeField
    # author_many = models.ManyToManyField('NewUser')


    def __str__(self):
        return f'The title is {self.title}'

    def get_absolute_url(self):
        return reverse("detail_class_blog", kwargs={"pk": self.pk, 'slug': self.slug_field})

    def save(self, *args, **kwargs):
        self.slug_field = self.title.replace(' ', '-')
        # self.author = self.request.user
        # print(self.request, args, kwargs)
        return super().save(*args, **kwargs)

    # def clean_fields(self, *args, **kwargs):
    #     print(self.request)
    #     return super().clean_fields(*args, **kwargs)


class NewUser(AbstractUser):
    contact = models.CharField(null=True, blank=True, max_length=240)
    image = models.ImageField(null=True, blank=True)
    # is_editor = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    # is_viewer = models.BooleanField(default=False)
    CHOICES = (
        (1, 'Admin'),
        (2, 'Editor'),
        (3, 'Viewer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=CHOICES, default=1)


class Profile(models.Model):
    user = models.OneToOneField(NewUser, on_delete=CASCADE)
    address = models.CharField(max_length=434)


class Comment(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(NewUser, on_delete=CASCADE)
    blog = models.ForeignKey(Blog, on_delete=CASCADE)