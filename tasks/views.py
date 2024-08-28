from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DeleteView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy

class LoginView(TemplateView):
    template_name = 'login.html'

class HomeView(TemplateView):
    template_name = 'home.html'


class UpdateTaskView(UpdateView):
    template_name = 'update.html'
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('list')


class CreateTaskView(CreateView):
    template_name = 'create.html'
    model = Task
    # form_class = TaskForm
    fields = '__all__'
    success_url = reverse_lazy('list')


class ListTaskView(ListView):
    template_name = 'list.html'
    model = Task

    def get_queryset(self, *args, **kwargs):
        qs= Task.objects.all().order_by('created_at')
        completed = self.request.GET.get('completed') == 'on'

        if completed:
            qs = qs.filter(completed=completed)

        return qs



class DeleteTaskView(DeleteView):
    template_name = 'delete.html'
    model = Task
    success_url = reverse_lazy('list')