from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'tast-list/',
        'Detail View':'/=detail-view/<str:pk>/',
        'Create':'create/',
        'update':'update/<str:pk>/',
        'delete':'delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    task = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item succussfuly deleted")
