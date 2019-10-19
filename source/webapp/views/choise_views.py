from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import PollChoiseForm, ChoiseForm
from webapp.models import Choise, Poll


class ChoiseForPullCreateView(CreateView):
    model = Choise
    form_class = PollChoiseForm
    template_name = 'choise/create.html'

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choises.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)

class ChoiseUpdateView(UpdateView):
    model = Choise
    template_name = 'choise/update.html'
    form_class = ChoiseForm
    context_object_name = 'choise'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})

class ChoiseDeleteView(DeleteView):
    model = Choise
    template_name = 'choise/delete.html'
    context_object_name = 'choise'
    success_url = reverse_lazy('index')

