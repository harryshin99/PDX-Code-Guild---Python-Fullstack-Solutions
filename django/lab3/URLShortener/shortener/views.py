from django.shortcuts import render, get_object_or_404, redirect
from .models import ShortenedURL
from django.urls.base import reverse
from django.http import HttpResponseRedirect

import random
import string

# Create your views here.
def index(req):
    urls = ShortenedURL.objects.all()
    context = {
        'urls': urls
    }
    return render(req, 'shortener/index.html', context)

def save_url(req):
    characters = string.ascii_letters + string.digits
    code = ""
    while len(code) < 5:
        code += random.choice(characters)
    
    url = req.POST['url']
    # form = req.POST
    # url = form['url']
    
    shortened_url = ShortenedURL(code=code, url=url)
    shortened_url.save()
    
    return HttpResponseRedirect(reverse('shortener:index'))

def forward(req, code):
    if len(code) != 5:
        return HttpResponseRedirect(reverse('shortener:index'))
    
    shortened_url = get_object_or_404(ShortenedURL, code=code)
    shortened_url.counter += 1
    shortened_url.save()
    url = shortened_url.url

    return redirect(url)
        