from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required


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
            task_list = Task.objects.filter(user=request.user)
            task_form = TaskForm(request.POST)
            return render(request, 'task/home.html', {'task': task_form, 'error': 0, 'list': task_list})


@login_required
def task_update(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        task = Task.objects.get(pk=int(task_id))
        status = request.POST.get('status')
        priority = request.POST.get('priority')
        if task.user == request.user:
            if status:
                task.status = status
            if priority:
                task.priority = priority
            task.save()
            return HttpResponse('updated')


@login_required
def task_delete(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        task = Task.objects.get(pk=int(task_id))
        if task.user == request.user:
            task.delete()
            return HttpResponse('deleted')

