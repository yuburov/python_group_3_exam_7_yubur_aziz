from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from webapp.forms import PollForm
from webapp.models import Poll, Choise, Answer


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    paginate_by = 5
    paginate_orphans = 1
    ordering = ['-created_at']

class PollView(DetailView):
    template_name = 'poll/poll.html'
    context_key = 'poll'
    model = Poll

class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class PollUpdateView(UpdateView):
    template_name = 'poll/update.html'
    form_class = PollForm
    model = Poll
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/delete.html'
    context_object_name = 'poll'
    model = Poll
    success_url = reverse_lazy('index')

class PollAnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choises = poll.choises.all()
        context = {
            'poll': poll,
            'choises': choises
        }
        return render(request, 'poll/answer.html', context)

    def post(self, request, *args, **kwargs):
        pk = request.POST['answer']
        choise = get_object_or_404(Choise, pk=pk)

        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(choise=choise, poll=poll)
        return redirect('index')
