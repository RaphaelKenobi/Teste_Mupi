from django.conf import settings
from django.shortcuts import render
from django.views.defaults import page_not_found
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import InsereTaskForm


class HomeView(TemplateView):
    template_name = 'home.html'


class ListTaskView(ListView):
    template_name = 'list.html'
    model = Task

    def get_queryset(self, *args, **kwargs):
        qs = Task.objects.all().order_by('created_at')
        completed = self.request.GET.get('completed') == 'on'

        if completed:
            qs = qs.filter(completed=completed)

        return qs


class UpdateTaskView(UpdateView):
    template_name = 'update.html'
    model = Task
    fields = '__all__'


class DeleteTaskView(DeleteView):
    template_name = 'delete.html'
    model = Task
    success_url = reverse_lazy('list')


class CreateTaskView(CreateView):
    template_name = 'create.html'
    model = Task
    form_class = InsereTaskForm
    success_url = reverse_lazy('list')


# ----------------------------------------------------------------------
def handler404(request, exception):
    return page_not_found(request, exception, template_name='404.html')
