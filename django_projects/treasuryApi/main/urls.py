from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('accounting/<int:pk>/', accounting, name='accounting'),
]
