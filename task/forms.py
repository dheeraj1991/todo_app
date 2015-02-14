from django import forms


class TaskForm(forms.Form):
    CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Task Name'}))
    description = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Enter the description here', 'style': 'height:130px;'}))
    priority = forms.ChoiceField(label='', widget=forms.Select(attrs={'placeholder': 'Priority'}), choices=CHOICES)
    due_date = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'Due Date'}))