from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

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



@csrf_protect
def add_blog(request):
    if request.method == "POST":
        print("POST mehtod called s---------------------------")
        print(request.POST)
        title = request.POST["title"]
        content = request.POST["content"]
        image = request.FILES["image"]
        print("Title = ",title, "Content  = ",content, "Image = ", image)
        fs = FileSystemStorage()
        print("IMage attribute =======", image.name)
        name = "blogs/"+ image.name
        print(name)
        fs.save(name=name, content=image)
        # image_url = fs.url(name=image.name)
        # print(fs.url(name=image.name), fs.path(name=image.name))
        # save_blog(title, content, image_url)
    return render(request, 'add_blog.html') 