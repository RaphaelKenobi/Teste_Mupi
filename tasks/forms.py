from django import forms
from .models import Task

class InsertTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'due_data']
        widgets = {
            'completed': forms.CheckboxInput(),
            'due_data': forms.DateInput(attrs={'type': 'date'}),
        }