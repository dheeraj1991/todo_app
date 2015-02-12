from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from datetime import date


def normal_check(user):
    if user.is_authenticated():
        return False
    else:
        return True


class Task_Page(View):

    @method_decorator(login_required)
    def get(self, request):
        task_list = Task.objects.filter(user=request.user)
        task_form = TaskForm()
        return render(request, 'task/home.html', {'task': task_form, 'list': task_list})

    @method_decorator(login_required)
    def post(self, request):
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            cleaned_data = task_form.cleaned_data
            task = Task(user=request.user, name=cleaned_data['name'], description=cleaned_data['description'],
                        priority=cleaned_data['priority'], due_date=cleaned_data['due_date'])
            task.save()
            return HttpResponseRedirect('/task/home/')
        else:
            task_form = TaskForm(request.POST)
            return render(request, 'task/home.html', {'task': task_form, 'error': 0})