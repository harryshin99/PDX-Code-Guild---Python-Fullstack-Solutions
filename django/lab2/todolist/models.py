from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    description = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True, default=None)

    