from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question

#from django.template import loader
# Create your views here.

#displays latest few entries
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)
    # template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request))

#displays a question with a form to vote
def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404(" Question does not exist")

#displays results for a question
def results(request, question_id):
    response = " You're looking at the results of question %s."
    return HttpResponse(response %question_id)
# handling voting for a question
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)
