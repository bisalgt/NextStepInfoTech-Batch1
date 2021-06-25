from django.urls import path

from blog.views import BlogCreateView, home, index, add_blog, detail_blog, delete_blog, update_blog, BlogListView

urlpatterns = [
    path('home/', home, name='home'),
    path('index/', index, name='index'),
    path('add_blog/', add_blog, name='add_blog'),
    path('detail/<int:id>/', detail_blog, name='detail_blog'),
    path('delete/<int:id>/', delete_blog, name='delete_blog'),
    path('update/<int:id>/', update_blog, name='update_blog'),
    path('list-blog/', BlogListView.as_view(), name='list_blog'),
    path('create-blog/', BlogCreateView.as_view(), name='create_blog'),
]


# detail_blog(request, id)
# delete_blog(request, id)