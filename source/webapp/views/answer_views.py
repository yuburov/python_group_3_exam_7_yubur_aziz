from django.views.generic import ListView
from webapp.models import Answer


class AnswerIndexView(ListView):
    template_name = 'answer/index.html'
    context_object_name = 'answers'
    model = Answer
    ordering = '-created_at'
    paginate_by = 5
    paginate_orphans = 1