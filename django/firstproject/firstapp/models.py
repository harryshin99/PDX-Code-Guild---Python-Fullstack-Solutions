from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=100)
    date_published = models.DateTimeField()

    def __str__(self):
        return self.author + ' - ' + self.title