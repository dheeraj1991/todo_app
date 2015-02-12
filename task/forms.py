from django import forms
from .models import Task
from django.forms.widgets import Textarea, DateInput


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ['user', 'status', ]
        widgets = {
            'description': Textarea(),
            'due_date': DateInput(),
        }