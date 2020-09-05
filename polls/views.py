from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from polls.models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from django.views import generic
#from django.template import loader
# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list' : latest_question_list}
#     return render(request, 'polls/index.html', context)
#     # template = loader.get_template('polls/index.html')
#     #return HttpResponse(template.render(context, request))
#

# def details(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/details.html', {'question': question})
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404(" Question does not exist")
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html',{'question': question})

#displays latest few entries
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        ''' return last 5 published questions '''
        return Question.objects.order_by('_pub_date')[:5]

# displays a question with a form to vote
class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

#displays results for a question
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# handling voting for a question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # if choice not in POST data raise keyerror
        # redisplay the question voting form
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # redirect to results if user tries to vote twice
        #reverse to pass control to results func in views
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))
