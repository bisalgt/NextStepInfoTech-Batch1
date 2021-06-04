from django.http import HttpResponse
from django.shortcuts import render

from django.db import connection

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
