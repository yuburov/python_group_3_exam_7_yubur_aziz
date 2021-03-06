from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=2000,null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question



class Choise(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    poll = models.ForeignKey('webapp.Poll',related_name='choises', on_delete=models.CASCADE, verbose_name='Опрос' )

    def __str__(self):
        return self.text

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='answers', on_delete=models.CASCADE, verbose_name='Опрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    choise = models.ForeignKey('webapp.Choise', related_name='answers', on_delete=models.CASCADE, verbose_name='Вариант ответа')

    def __str__(self):
        return "{} | {}".format(self.poll, self.choise)