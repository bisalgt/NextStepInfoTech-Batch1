from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug_field = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'The title is {self.title}'

    def get_absolute_url(self):
        return reverse("detail_class_blog", kwargs={"pk": self.pk, 'slug': self.slug_field})