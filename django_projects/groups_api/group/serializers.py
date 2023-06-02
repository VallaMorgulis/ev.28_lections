from rest_framework import serializers
from .models import Teacher, Student, Group

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id', 'title', 'teacher_name')
#
#         def teacher_name(self, obj):
#             return obj



