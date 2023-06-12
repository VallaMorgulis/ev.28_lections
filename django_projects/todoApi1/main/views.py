from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Task
from main.serializer import TaskSerializer


@api_view(['GET', 'POST'])
def task_create_list_view(request):
    if request.method == 'GET':
        queryset = Task.objects.all()
        serializer = TaskSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)
    else:
        data = request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
