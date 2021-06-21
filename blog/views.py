from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

from .forms import BlogForm

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


