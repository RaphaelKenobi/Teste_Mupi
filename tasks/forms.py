from django import forms
from .models import Task


class InsereTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_data', 'user']
        delete = ['delete']

