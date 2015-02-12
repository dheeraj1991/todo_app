from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import TaskForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout


def normal_check(user):
    if user.is_authenticated():
        return False
    else:
        return True

# Create your views here.
class Task(View):

    @method_decorator(user_passes_test(normal_check, login_url='/user/login/'))
    def get(self, request):
        task_form = TaskForm()
        return render(request, 'task/home.html', {'task': task_form})