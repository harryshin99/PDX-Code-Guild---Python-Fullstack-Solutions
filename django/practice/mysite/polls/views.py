from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question, Choice

def index(request):
    questions = Question.objects.order_by('-pub_date')
    context = {
        'questions': questions
    }
    return render(request, '/polls/index.html')

def detail(request, id):
    question = get_object_or_404(Question, id=id)
    context = {
        'question': question
    }
    return render(request, '/polls/detail.html', context)

def results(request, id):
    return HttpResponse(f'You\'re looking at the results of question {id}')

def vote(request, id):
    return HttpResponse(f'You\'re voting on question {id}')