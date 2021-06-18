from django.urls import path

from blog.views import home, index, add_blog

urlpatterns = [
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('add_blog/', add_blog, name='add_blog'),
]