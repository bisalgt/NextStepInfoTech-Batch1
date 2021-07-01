from django.urls import path

from blog.views import BlogCreateView, home, index, add_blog, detail_blog, delete_blog, update_blog, \
    BlogListView, BlogBasicView, BlogDetailView, UserCreateView, UserUpdateView

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('add_blog/', add_blog, name='add_blog'),
    path('detail/<int:id>/', detail_blog, name='detail_blog'),
    path('delete/<int:id>/', delete_blog, name='delete_blog'),
    path('update/<int:id>/', update_blog, name='update_blog'),
    path('list-blog/', BlogListView.as_view(), name='list_blog'),
    path('create-blog/', BlogCreateView.as_view(), name='create_blog'),
    path('basic-blog/', BlogBasicView.as_view(), name='basic_blog'),
    path('detail-blog/<int:pk>/<slug:slug>/', BlogDetailView.as_view(), name='detail_class_blog'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('update-user/<int:pk>/', UserUpdateView.as_view(), name='update-user'),
]


# detail_blog(request, id)
# delete_blog(request, id)