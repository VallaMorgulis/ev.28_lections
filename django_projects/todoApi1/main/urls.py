from django.urls import path

from .views import task_create_list_view

urlpatterns = [
    path('tasks/', task_create_list_view),
]