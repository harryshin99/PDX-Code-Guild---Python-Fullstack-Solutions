from django.db import models

# Create your models here.

class Priority(models.Model):
    name = models.CharField(max_length=6)
    objects = models.Manager()

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True, default=None)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="todo_items", blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.description