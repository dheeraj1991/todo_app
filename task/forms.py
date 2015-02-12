from django import forms
from .models import Task


class TaskForm(forms.Form):

    class Meta:
        model = Task
        fields = ['name', 'description', 'priority', 'due_date']

    # def clean(self):
