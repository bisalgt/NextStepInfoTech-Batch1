from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print('home function called')
    return render(request, 'home.html')

def index(request):
    print('index function called')

    context = {'blogs': [{'blogheading': 'Blog Heading 1', 'blogcontent': 'THis is the content of blog 1'}, \
    { 'blogheading': 'Blog Heading 2', 'blogcontent': 'THis is the content of blog 2'}, { 'blogheading': 'Blog Heading 3', \
     'blogcontent': 'THis is the content of blog 3'}, { 'blogheading': 'Blog Heading 4', 'blogcontent': 'THis is the content of blog 4'}, \
     { 'blogheading': 'Blog Heading 5', 'blogcontent': 'THis is the content of blog 5'}]}

    return render(request, 'index.html', context)