from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_protect

def home(request):
    print('home function called')
    return HttpResponse("<h1>Hello World!</h1>")

@csrf_protect
def index(request):
    print('index function called')
    if request.method == "POST":
        print(request.POST)
    return render(request, 'index.html')