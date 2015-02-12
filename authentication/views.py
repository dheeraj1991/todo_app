from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout


def normal_check(user):
    if user.is_authenticated():
        return False
    else:
        return True


class SignUp(View):

    @method_decorator(user_passes_test(normal_check, login_url='/task/home/'))
    def get(self, request):
        signup_form = SignUpForm()
        return render(request, 'authentication/signup.html', {'signup': signup_form})

    @method_decorator(user_passes_test(normal_check, login_url='/task/home/'))
    def post(self, request):
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            login_form = LoginForm()
            return render(request, 'authentication/login.html', {'login': login_form})
        else:
            signup_form = SignUpForm(request.POST)
            return render(request, 'authentication/signup.html', {'signup': signup_form})


class Login(View):

    @method_decorator(user_passes_test(normal_check, login_url='/task/home/'))
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'authentication/login.html', {'login': login_form})

    @method_decorator(user_passes_test(normal_check, login_url='/task/home/'))
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data
            login(request, user)
            return render(request, 'task/home.html',)
        else:
            login_form = LoginForm(request.POST)
            return render(request, 'authentication/login.html', {'login': login_form})
