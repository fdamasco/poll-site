from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from datetime import datetime
from .forms import QuestionForm

from django.views import generic
from django.views.generic import CreateView
from django.utils import timezone


from .models import Choice, Question



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            visible=True
        ).order_by('pub_date')

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')


def createQuestion(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)

        if form.is_valid():
            polls = form.save(commit=False)
            polls.done = 'doing'
            polls.save()
            return HttpResponseRedirect("/")
            #return redirect('/')
            #return render(request, 'polls/index')

    else:
        form = QuestionForm()
        return render(request, 'polls/question_create.html', {'form': form})


# class QuestionCreate(CreateView):
#     model = Question
#     fields = ('question_text', 'limit_date',)
#     success_url = reverse_lazy('polls/')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    extra_context = {'now': timezone.now}

    def get_queryset(self):
        if timezone.now() > timezone.make_aware(datetime(2022, 12, 18)):
            return Question.objects.none()
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))





