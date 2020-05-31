from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
# Create your views here.

from .models import Questions,Choice

def index(request):
    latest_ques_list=Questions.objects.order_by('-pub_date')[:5]
    context={'latest_ques_list':latest_ques_list}
    return render(request,'Polls/index.html',context)

def detail(request,ques_id):
    try:
        question=Questions.objects.get(pk=ques_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exit")
    return render(request,'Polls/detail.html',{'question':question})

def results(request,ques_id):
    question=get_object_or_404(Questions,pk=ques_id)
    return render(request,'Polls/results.html',{'question':question})

def vote(request, ques_id):
    question=get_object_or_404(Questions,pk=ques_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',
        {
            'question':question,
            'error_message':"You did not select anything.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def addpoll(request):
    return render(request,'Polls/addpoll.html')