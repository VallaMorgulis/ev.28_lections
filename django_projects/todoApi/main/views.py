import generics as generics
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from main.models import Task
from main.serializers import TaskSerializer, TaskListSerializer


# Class based-view
# 3 вида
# APIView, Generics, ViewSet


# generics
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()

    # serializer_class = TaskSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskListSerializer
        return TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListCreateApiView(APIView):
    def get(self, request):
        queryset = Task.objects.all()
        serializer = TaskListSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


class TaskDetailApiView(APIView):
    @staticmethod
    def _get_object(pk):
        try:
            return Task.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk):
        queryset = self._get_object(pk)
        serializer = TaskSerializer(instance=queryset)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        queryset = self._get_object(pk)
        serializer = TaskSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        queryset = self._get_object(pk)
        serializer = TaskSerializer(instance=queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        queryset = self._get_object(pk)
        queryset.delete()
        return Response('Successfully deleted!', status=204)


# function based-view

@api_view(['GET', 'POST'])
def task_create_list_view(request):
    if request.method == 'GET':
        queryset = Task.objects.all()
        serializer = TaskListSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)
    else:
        data = request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def task_detail_view(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return Response(f'This task, with {pk} id, does not exist!', status=404)
    if request.method == 'GET':
        serializer = TaskSerializer(instance=task)
        return Response(serializer.data, status=200)
    elif request.method in ('PUT', 'PATCH'):
        serializer = TaskSerializer(instance=task,
                                    data=request.data) if request.method == 'PUT' else TaskSerializer(instance=task,
                                                                                                      data=request.data,
                                                                                                      partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=206)
    else:
        task.delete()
        return Response('Successfully deleted!', status=204)

# Сырой вариант не используя библиотеки

# def task_list(request):
#     tasks = Task.objects.all()
#     print(tasks, '!!!!!!!!!!!!!!!!!')
#     ls = []
#     for task in tasks:
#         dict_ = {'id': task.id, 'title': task.title,
#                  'description': task.description, 'deadline': str(task.deadline)}
#         ls.append(dict_)
#         # print(dict_, '!!!!!!!!!!!!!!!!!!!!!!')
#     json_result = json.dumps(ls)
#     return HttpResponse(json_result, content_type='application/json')
#
#
# def task_create(request):
#     data = request.body
#     print(data, '********************')
#     res = json.loads(data)
#     print(res, "!!!!!")
#     title = res['title']
#     desc = res['description']
#     deadline = datetime.strptime(res['deadline'], '%Y-%m-%d')
#     print(title, desc, deadline)
#     obj = Task.objects.create(title=title, description=desc, deadline=deadline)
#     return HttpResponse(obj)
