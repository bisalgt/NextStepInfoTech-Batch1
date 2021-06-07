from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_protect, csrf_exempt

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
    context = {'blogs': blogs}
    print(context)
    return render(request, 'index.html', context)

def save_blog(title, content):
    with connection.cursor() as cursor:
        query = "INSERT INTO blogs (heading, content) VALUES (%s, %s)"
        list_of_values = [title, content]
        cursor.execute("INSERT INTO blogs (heading, content) VALUES (%s, %s)", [title, content])
        # cursor.execute(query, list_of_values)
    return True



@csrf_protect
def add_blog(request):
    if request.method == "POST":
        print("POST mehtod called s---------------------------")
        print(request.POST)
        title = request.POST["title"]
        content = request.POST["content"]
        print("Title = ",title, "Content  = ",content)
        save_blog(title, content)
    return render(request, 'add_blog.html') 