from django.urls import path

from .views import rest_blog_view, rest_blog_detail, rest_blog_view_new

urlpatterns = [
    path('', rest_blog_view),
    path('new/', rest_blog_view_new),
    path('detail/<int:id>/', rest_blog_detail),
]
