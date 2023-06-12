from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    deadline = models.DateField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


