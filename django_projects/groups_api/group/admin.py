from django.contrib import admin

from group.models import Teacher, Group, Student

# admin.site.register(Teacher)


# admin.site.register(Group)
# admin.site.register(Student)


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'students', 'count_of_students')

    def count_of_students(self, obj):
        print(obj, '!!!!!!!!!!!!!!!!!!')
        qt = obj.student.count()
        print(qt, '111111111111111')
        print()
        return qt

    def students(self, obj):
        return [x for x in obj.student.all()]


@admin.register(Student)
class Students(admin.ModelAdmin):
    list_display = ('student_name', 'groups_list')

    def student_name(self, obj):
        return obj

    def groups_list(self, obj):
        # print(obj.id, obj.name, obj.last_name, obj.age, obj.contacts)
        # print(obj.groups.all(), '!!!!!!!!')
        return [x for x in obj.groups.all()]


@admin.register(Teacher)
class Teachers(admin.ModelAdmin):
    list_display = ('teacher_name', 'language')

    def teacher_name(self, obj):
        return obj
