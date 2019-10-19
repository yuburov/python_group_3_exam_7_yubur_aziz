from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm
from webapp.models import Poll


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