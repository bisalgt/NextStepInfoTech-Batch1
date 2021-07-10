from django.http import JsonResponse
from django.http.response import Http404
from django.views.decorators import csrf
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import BlogSerializer
from .models import RestBlog

@csrf_exempt
def rest_blog_view(request):
    if request.method=='GET':
        serializer = BlogSerializer(RestBlog.objects.all(), many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method=='POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return Http404()

@csrf_exempt
def rest_blog_detail(request, id):
    blog = RestBlog.objects.get(id=id)
    if request.method=='GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data, safe=False)

    if request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return Http404()

    if request.method=='DELETE':
        # RestBlog.objects.delete(id=id)
        blog.delete()
        return JsonResponse({'status': 'done'})


from rest_framework.decorators import api_view
from rest_framework.response import Response

@csrf_exempt
@api_view(['GET'])
def rest_blog_view_new(request):
    if request.method=='GET':
        serializer = BlogSerializer(RestBlog.objects.all(), many=True)
        return Response(serializer.data)
    if request.method=='POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return Http404()