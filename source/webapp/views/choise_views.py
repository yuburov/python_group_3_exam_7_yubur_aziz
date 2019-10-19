class PollCreateView(CreateView):
    template_name = 'poll/create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})
