from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.db import connection
from django.urls.base import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView
from django.urls import reverse

from .forms import BlogForm, BlogModelForm
from .models import Blog

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


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogModelForm
    template_name = 'create_blog.html'
    success_url = reverse_lazy('list_blog')

