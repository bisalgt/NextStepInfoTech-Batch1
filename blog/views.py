from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.db import connection
from django.urls.base import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView
from django.urls import reverse
from django.views import View
from django.views.generic.detail import DetailView


from .forms import BlogForm, BlogModelForm
from .models import Blog, NewUser

def home(request):
    print('home function called')
    return render(request, 'home.html')


def my_custom_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM blogs", [])
        blogs = cursor.fetchall()
    return blogs

def index(request):
    print('index function called ------------------------------------------------------')
    blogs = my_custom_sql()
    paginator = Paginator(blogs, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

def save_blog(title, content, image_url):
    with connection.cursor() as cursor:
        # query = "INSERT INTO blogs (heading, content, image) VALUES (%s, %s, %s)"
        # list_of_values = [title, content]
        cursor.execute("INSERT INTO blogs (heading, content, image) VALUES (%s, %s, %s)", [title, content, image_url])
        # cursor.execute(query, list_of_values)
    return True



def add_blog(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # print('======================',request.POST,'=============================')
        # print('0000000======',request.FILES,'=============================')
        form = BlogForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # print("-------------------------", form.cleaned_data)

            title = form.cleaned_data["title"]
            content =  form.cleaned_data.get('content')
            image = form.cleaned_data.get('image', "NO IMage")
            
            fs = FileSystemStorage()
            image_name = f'{title}_image.jpg'
            fs.save(image_name,content=image)
            print(fs.url(image_name))
            # print(title, content, image)
            save_blog(title, content, fs.url(image_name))
            return redirect("index")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BlogForm()

    return render(request, 'add_blog.html', {'form': form})

def detail_blog_sql(id):
    with connection.cursor() as cursor:
        query = "SELECT * FROM blogs WHERE id=%s"
        place_holders = [id]
        cursor.execute(query, place_holders)
        blog = cursor.fetchone()
    return blog



def detail_blog(request,id):
    blog = detail_blog_sql(id)
    print(id, type(id))
    return render(request, 'blog_detail.html', {'blog': blog})


def delete_blog_sql(id):
    try:
        with connection.cursor() as cursor:
            query = "DELETE FROM blogs WHERE id=%s"
            place_holders = [id]
            cursor.execute(query, place_holders)
    except Exception as e:
        return False
    return True


def delete_blog(request, id):
    result = delete_blog_sql(id)
    if result:
        return render(request, 'blog_delete.html', {'id': id})
    else:
        return HttpResponse("Blog doesnot exists")




# def update_blog_sql(id):
#     try:
#         with connection.cursor() as cursor:
#             query = "UPDATE FROM blogs WHERE id=%s"
#             place_holders = [id]
#             cursor.execute(query, place_holders)
#     except Exception as e:
#         return False
#     return True


def update_blog(request, id):
    blog = detail_blog_sql(id)
    form = BlogForm({'title': blog[1], 'content': blog[2]})
    return render(request, 'update_blog.html', {'form': form})


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'list_blog.html'

from django.contrib.auth.mixins import LoginRequiredMixin

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogModelForm
    template_name = 'create_blog.html'
    # success_url = reverse_lazy('list_blog')

    # def post(self, *args, **kwargs):
    #     print("This is inside the post -------------------------")
    #     self.author = self.request.user
    #     return super().post(*args, **kwargs)

    def form_invalid(self, *args, **kwargs):
        print("Form is invalid ")
        return super().form_invalid(*args, **kwargs)

    def form_valid(self, *args, **kwargs):
        print("Form is Valid")
        # print(dir(self))
        print(self.request.user, ' Current User ')
        print(self.fields)
        print(args, kwargs)
        print(args[0].fields)
        # args[0].fields["author"] = self.request.user
        args[0].instance.author = self.request.user
        return super().form_valid(*args, **kwargs)



class BlogBasicView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class BlogDetailView(DetailView):
    model = Blog # list of objects to search
    # url--- pk; search for object whose pk value is pk
    # query_pk_and_slug = True
    slug_field = 'slug_field'
    template_name = 'blog_detail.html'

    # def get(self):
    #     print(self)
    #     super().get(self.request)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["key"] = 'value'
    #     print(context)
    #     return context



from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import UpdateView
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import NewUser
from .forms import CreateUserForm, UpdateForm

class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = NewUser
    form_class = CreateUserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        print(self.request.user)
        print('USer passes test = ', self.request.user.user_type)
        print(self.request.user.user_type==1)
        return self.request.user.user_type in [1, 2]



class UserUpdateView(UpdateView):
    model = NewUser
    form_class = UpdateForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('home')


# class DetailUserView

from django.contrib.auth import authenticate, login, logout


# DELTEVIEW, UPDATEVIEW

from django.views.decorators.csrf import csrf_protect, csrf_exempt

# @csrf_exempt
# @login_required
def ajax_view(request):
    # print(request.GET)
    print(request.POST)
    print(request.user)
    # Comments.objects.create(title='',author= )
    print("this function is called")
    
    return HttpResponse('hello  world')