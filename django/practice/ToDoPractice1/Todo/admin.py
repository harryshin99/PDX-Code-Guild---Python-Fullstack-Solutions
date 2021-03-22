from django.contrib import admin

# Register your models here.
from .models import ToDoItem, Priority

admin.site.register(ToDoItem)

admin.site.register(Priority)