from django import forms
from .models import Task


class TaskForm(forms.Form):
    model = Task
    fields = '__all__'
