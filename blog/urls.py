from django.urls import path

from blog.views import home, index

urlpatterns = [
    path('home/', home, name='home'),
    path('index/', index, name='index'),
]