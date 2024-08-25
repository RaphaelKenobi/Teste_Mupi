from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # class Meta:
    #     verbose_name = 'Tarefa'

    title = models.CharField(max_length=100,verbose_name='Título da tarefa')
    description = models.TextField(verbose_name='Descrição detalhada da tarefa')
    completed = models.BooleanField(default=False,verbose_name='Foi concluída?')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Criado em')
    due_data = models.DateTimeField(null=True, blank=True,verbose_name='Prazo')
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE,verbose_name='Usuário responsável pela tarefa')

    def __str__(self):
        return self.title
