from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DeleteView
from .models import Task
from .forms import TaskForm
from django.urls import reverse_lazy
class HomeView(TemplateView):
    template_name = 'home.html'


class UpdateTaskView(UpdateView):
    template_name = 'update.html'
    model = Task


class CreateTaskView(CreateView):
    template_name = 'create.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('home')


class ListTaskView(ListView):
    template_name = 'list.html'
    model = Task


class DeleteTaskView(DeleteView):
    template_name = 'delete.html'
    model = Task
