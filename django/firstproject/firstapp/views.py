from django.shortcuts import render
from .models import BlogPost
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse('<h1> hello world </h1>')

def index(request):

    blog_posts = BlogPost.objects.all()

    context = {
        "blog_posts": blog_posts
    }
    return render(request, 'firstapp/index.html', context)