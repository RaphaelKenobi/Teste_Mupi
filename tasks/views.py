from django.views.defaults import page_not_found
from django.views.generic import TemplateView, UpdateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, get_object_or_404
from .forms import InsereTaskForm


class HomeView(TemplateView):
    template_name = 'home.html'


@method_decorator(login_required, name='dispatch')
class ListTaskView(ListView):
    template_name = 'list.html'
    model = Task

    def get_queryset(self):
        # Filtra as tasks para mostrar apenas as criadas pelo usuário logado
        return Task.objects.filter(user=self.request.user).order_by('created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed = self.request.GET.get('completed') == 'on'

        # Filtra o queryset se a opção 'completed' estiver marcada
        if completed:
            context['object_list'] = context['object_list'].filter(completed=True)

        return context


class UpdateTaskView(UpdateView):
    template_name = 'update.html'
    model = Task
    fields = ['title', 'description', 'completed', 'due_data']
    success_url = reverse_lazy('list')


class DeleteTaskView(DeleteView):
    template_name = 'delete.html'
    model = Task
    success_url = reverse_lazy('list')


class CreateTaskView(CreateView):
    template_name = 'create.html'
    model = Task
    form_class = InsereTaskForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# ----------------------------------------------------------------------
def handler404(request, exception):
    return page_not_found(request, exception, template_name='404.html')

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = True
        task.save()
        return redirect('list')
