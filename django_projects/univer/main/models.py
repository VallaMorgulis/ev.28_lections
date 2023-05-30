from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
